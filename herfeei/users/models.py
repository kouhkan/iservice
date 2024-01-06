from django.db import models
from herfeei.common.models import BaseModel

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _


class BaseUserManager(BUM):
    def create_user(self, username, email=None, password=None):
        if not email:
            raise ValueError(_("Users must have an email address"))

        user = self.model(username=username, email=self.normalize_email(email.lower()))

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )

        user.role = BaseUser.UserRole.ADMIN
        user.save(using=self._db)

        return user


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    class UserRole(models.TextChoices):
        ADMIN = "ADMIN"
        USER = "USER"
        EXPERT = "EXPERT"

    username = models.CharField(_("Phone number"), max_length=14, unique=True, db_index=True)
    email = models.EmailField(_("email address"), unique=True, db_index=True, null=True, blank=True)
    role = models.CharField(max_length=9, choices=UserRole.choices, default=UserRole.USER)

    objects = BaseUserManager()

    def __str__(self):
        return self.username

    def is_staff(self):
        return self.role == self.UserRole.ADMIN

    def is_admin(self):
        return self.role == self.UserRole.ADMIN


class Profile(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.user} >> {self.bio}"
