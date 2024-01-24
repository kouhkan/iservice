from typing import List

from django.db.models import QuerySet

from herfeei.notifications.models import UserNotification
from herfeei.users.models import BaseUser


def get_user_notifications(*,
                           user: BaseUser) -> List[QuerySet[UserNotification]]:
    return UserNotification.objects.filter(user=user)


def get_user_notifications_by_category(
        *, user: BaseUser,
        category_slug: str) -> List[QuerySet[UserNotification]]:
    return UserNotification.objects.filter(
        user=user, notification__category__slug=category_slug)


def get_user_unread_notifications(
        *, user: BaseUser) -> List[QuerySet[UserNotification]]:
    return UserNotification.objects.filter(
        user=user, status=UserNotification.NotificationStatus.UNREAD)


def get_user_read_notifications(
        *, user: BaseUser) -> List[QuerySet[UserNotification]]:
    return UserNotification.objects.filter(
        user=user, status=UserNotification.NotificationStatus.READ)
