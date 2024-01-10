from django.contrib.auth import get_user_model
from django.db import models

from herfeei.common.models import BaseModel


class Notification(BaseModel):
    class NotificationLevel(models.TextChoices):
        DANGER = "DANGER"
        SUCCESS = "SUCCESS"
        WARNING = "WARNING"
        INFO = "INFO"

    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True, db_index=True, allow_unicode=True)
    description = models.TextField()
    level = models.CharField(max_length=10, choices=NotificationLevel.choices, default=NotificationLevel.INFO)

    def __str__(self):
        return self.title


class UserNotification(BaseModel):
    class NotificationStatus(models.TextChoices):
        READ = "READ"
        UNREAD = "UNREAD"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="notifications")
    notification = models.ForeignKey(Notification, on_delete=models.PROTECT, related_name="user")
    status = models.CharField(max_length=6, choices=NotificationStatus.choices, default=NotificationStatus.UNREAD)

    def __str__(self):
        return f"{self.user}"
