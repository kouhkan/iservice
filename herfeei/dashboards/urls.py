from django.urls import path, include
from rest_framework_simplejwt.views import TokenBlacklistView

from herfeei.dashboards.apis.users import UpdateUserAvatarView, UpdateUserProfileView
from herfeei.users.apis.addresses import CreateUserAddressView, GetUserAddressesListView, GetUserAddressView

urlpatterns = [
    path("", include([
        path("users/", include([
            path("avatar/", UpdateUserAvatarView.as_view(), name="avatar"),
            path("profile/", UpdateUserProfileView.as_view(), name="profile"),
        ])),
        path("logout/", TokenBlacklistView.as_view(), name="logout"),
        path("addresses/", include([
            path("", CreateUserAddressView.as_view(), name="create-address"),
            path("<int:id>/", GetUserAddressView.as_view(), name="get-user-address"),
            path("list/", GetUserAddressesListView.as_view(), name="get-user-addresses"),
        ]))
    ]))
]
