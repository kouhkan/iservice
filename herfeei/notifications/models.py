from django.contrib.auth import get_user_model
from django.db import models
from treebeard.mp_tree import MP_Node

from herfeei.common.models import BaseModel


class NotificationCategory(MP_Node, BaseModel):
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, db_index=True, unique=True, allow_unicode=True)

    class Meta:
        verbose_name_plural = "Notification Categories"

    def __str__(self):
        return self.title


class BaseNotification(BaseModel):
    class NotificationLevel(models.TextChoices):
        DANGER = "DANGER"
        SUCCESS = "SUCCESS"
        WARNING = "WARNING"
        INFO = "INFO"

    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True, db_index=True, allow_unicode=True)
    level = models.CharField(max_length=10, choices=NotificationLevel.choices, default=NotificationLevel.INFO)
    category = models.ForeignKey(NotificationCategory, on_delete=models.CASCADE, related_name="notification")

    def __str__(self):
        return self.title


class NotificationOption(BaseModel):
    item = models.CharField(max_length=128)
    value = models.CharField(max_length=256)

    def __str__(self):
        return self.item


class UserNotification(BaseModel):
    class NotificationStatus(models.TextChoices):
        READ = "READ"
        UNREAD = "UNREAD"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="notifications")
    notification = models.ForeignKey(BaseNotification, on_delete=models.PROTECT, related_name="user")
    status = models.CharField(max_length=6, choices=NotificationStatus.choices, default=NotificationStatus.UNREAD)
    options = models.ManyToManyField(NotificationOption, related_name="user_notifications")

    def __str__(self):
        return f"{self.user}"
