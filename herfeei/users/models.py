from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from herfeei.common.models import BaseModel


class BaseUserManager(BUM):
    def create_user(self, username, email=None, password=None):
        if not username:
            raise ValueError(_("Users must have an username that username is phone number"))

        user = self.model(username=username, email=self.normalize_email(email.lower())) \
            if email \
            else self.model(username=username)

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email=None, password=None):
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

    username = models.CharField(_("Phone number"), max_length=10, unique=True, db_index=True)
    email = models.EmailField(_("email address"), unique=True, db_index=True, null=True, blank=True)
    role = models.CharField(max_length=9, choices=UserRole.choices, default=UserRole.USER)

    objects = BaseUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def is_staff(self):
        return self.role == self.UserRole.ADMIN

    def is_superuser(self):
        return self.role == self.UserRole.ADMIN

    def __str__(self):
        return self.username

    class Meta:
        unique_together = (
            ("username", "email"),
        )


class Profile(BaseModel):
    class UserGender(models.TextChoices):
        MALE = "MALE"
        FEMALE = "FEMALE"
        OTHER = "OTHER"

    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    full_name = models.CharField(max_length=64, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    gender = models.CharField(max_length=9, choices=UserGender.choices, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"


class Address(BaseModel):
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name="addresses")
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True, db_index=True, allow_unicode=True)
    details = models.CharField(max_length=512)
    phone = models.CharField(max_length=10, null=True, blank=True)
    default = models.BooleanField(default=False)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    long = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    class Meta:
        unique_together = (
            ("lat", "long"),
        )

    def __str__(self):
        return f"{self.user}"
