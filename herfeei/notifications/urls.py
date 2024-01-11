from django.urls import path

from herfeei.notifications.apis.notifications import GetUserNotificationsView

urlpatterns = [
    path("", GetUserNotificationsView.as_view(), name="get-user-notifications"),
]
