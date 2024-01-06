from django.urls import path

from herfeei.users.apis.profiles import ProfileView

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
]
