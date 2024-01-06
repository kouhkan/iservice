from django.urls import path, include

urlpatterns = [
    path("users/", include(("herfeei.users.urls", "users"), namespace="users")),
]
