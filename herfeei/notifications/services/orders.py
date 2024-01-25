from herfeei.notifications.models import (BaseNotification,
                                          NotificationCategory,
                                          NotificationOption, UserNotification)
from herfeei.orders.models import Order


def notification_order_created(order: Order) -> UserNotification:
    notification_order_options = NotificationOption.objects.create(
        item="order_track_id", value=order.order_track_id
    )
    notification_order, _ = BaseNotification.objects.get_or_create(
        title="Order",
        slug="order",
        category=NotificationCategory.objects.filter(slug="order").first(),
        defaults={"slug": "order"}
    )
    user_notification = UserNotification.objects.create(
        user=order.user_answer.user,
        notification=notification_order
    )
    user_notification.options.set((notification_order_options,))
    return user_notification


def notification_order_completed(order: Order) -> UserNotification:
    notification_order_options = NotificationOption.objects.create(
        item="is_complete", value=order.is_complete,
    )
    notification_order, _ = BaseNotification.objects.get_or_create(
        title="Order",
        slug="order",
        category=NotificationCategory.objects.filter(slug="order").first(),
        defaults={"slug": "order"}
    )
    user_notification = UserNotification.objects.create(
        user=order.user_answer.user,
        notification=notification_order
    )
    user_notification.options.set((notification_order_options,))
    return user_notification
