from django.urls import path

from herfeei.users.apis.profiles import ProfileView, GetUserAvatarsView

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("avatars/", GetUserAvatarsView.as_view(), name="get-user-avatars"),
]
