from django.urls import path

from herfeei.notifications.apis.notifications import (GetUserNotificationsView,
                                                      ReadUserNotificationView)

urlpatterns = [
    path("", GetUserNotificationsView.as_view(),
         name="get-user-notifications"),
    path("read/<int:id>/",
         ReadUserNotificationView.as_view(),
         name="read-user-notification"),
]
