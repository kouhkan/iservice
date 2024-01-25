from herfeei.notifications.models import (BaseNotification,
                                          NotificationCategory,
                                          NotificationOption, UserNotification)
from herfeei.users.models import BaseUser


def notification_user_created(user: BaseUser) -> UserNotification:
    notification_order_options = NotificationOption.objects.create(
        item="phone_number", value=user.username
    )
    notification_order, _ = BaseNotification.objects.get_or_create(
        title="User",
        slug="user",
        category=NotificationCategory.objects.filter(slug="user").first(),
        level=BaseNotification.NotificationLevel.SUCCESS,
        defaults={"slug": "user"}
    )
    user_notification = UserNotification.objects.create(
        user=user,
        notification=notification_order
    )
    user_notification.options.set((notification_order_options,))
    return user_notification
