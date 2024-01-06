from django.urls import path

from herfeei.users.apis.profiles import ProfileView
from herfeei.users.apis.users import RegisterView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
