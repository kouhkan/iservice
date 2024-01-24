from herfeei.notifications.models import UserNotification
from herfeei.users.models import BaseUser


def change_to_read_notification(
        *, user: BaseUser, notification_id: int) -> UserNotification | bool:
    if not (notification := UserNotification.objects.filter(
            id=notification_id,
            user=user,
            status=UserNotification.NotificationStatus.UNREAD).first()):
        return False
    notification.status = UserNotification.NotificationStatus.READ
    notification.save()
    return notification
