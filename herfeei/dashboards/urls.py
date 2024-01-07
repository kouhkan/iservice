from django.urls import path, include
from rest_framework_simplejwt.views import TokenBlacklistView

from herfeei.dashboards.apis.users import UpdateUserAvatarView, UpdateUserProfileView

urlpatterns = [
    path("", include([
        path("users/", include([
            path("avatar/", UpdateUserAvatarView.as_view(), name="avatar"),
            path("profile/", UpdateUserProfileView.as_view(), name="profile"),
        ])),
        path("logout/", TokenBlacklistView.as_view(), name="logout"),
    ]))
]
