from django.urls import path, include

urlpatterns = [
    path("users/", include(("herfeei.users.urls", "users"), namespace="users")),
    path("auth/", include(("herfeei.authentication.urls", "users"), namespace="auth")),
]
