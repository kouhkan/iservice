from django.utils.text import slugify

from herfeei.notifications.models import UserNotification, Notification
from herfeei.users.models import BaseUser


def create_base_notification(
        *,
        title: str,
        description: str,
        level: Notification.NotificationLevel = Notification.NotificationLevel.INFO
) -> Notification:
    return Notification.objects.create(title=title, slug=slugify(title), description=description, level=level)


def create_welcome_notification(*, user: BaseUser) -> UserNotification:
    title = "خوش آمدید"
    description = f"کاربر {user} به اپلیکیشن حرفه‌ای خوش آمدید"
    notification = create_base_notification(title=title, description=description)
    return UserNotification.objects.create(user=user, notification=notification)


def read_notification(*, user: BaseUser, notification_id: int) -> UserNotification | bool:
    if not (notification := UserNotification.objects.filter(
            id=notification_id, user=user,
            status=UserNotification.NotificationStatus.UNREAD).first()
    ):
        return False
    notification.status = UserNotification.NotificationStatus.READ
    notification.save()
    return notification
