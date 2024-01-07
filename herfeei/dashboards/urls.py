from django.urls import path, include

from herfeei.dashboards.apis.users import UpdateUserAvatarView, UpdateUserProfileView

urlpatterns = [
    path("", include([
        path("users/", include([
            path("avatar/", UpdateUserAvatarView.as_view(), name="avatar"),
            path("profile/", UpdateUserProfileView.as_view(), name="profile"),
        ])),
    ]))
]
