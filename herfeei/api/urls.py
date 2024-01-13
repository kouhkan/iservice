from django.urls import path, include

urlpatterns = [
    path("users/", include(("herfeei.users.urls", "users"), namespace="users")),
    path("auth/", include(("herfeei.authentication.urls", "users"), namespace="auth")),
    path("dashboards/", include(("herfeei.dashboards.urls", "dashboards"), namespace="dashboards")),
    path("services/", include(("herfeei.services.urls", "services"), namespace="services")),
    path("notifications/", include(("herfeei.notifications.urls", "users"), namespace="notifications")),
    path("home/", include(("herfeei.home.urls", "home"), namespace="home")),
]
