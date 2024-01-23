from django.urls import path, include

urlpatterns = [
    path("users/", include(("herfeei.users.urls", "users"), namespace="users")),
    path("auth/", include(("herfeei.authentication.urls", "users"), namespace="auth")),
    path("dashboards/", include(("herfeei.dashboards.urls", "dashboards"), namespace="dashboards")),
    path("services/", include(("herfeei.services.urls", "services"), namespace="services")),
    path("notifications/", include(("herfeei.notifications.urls", "users"), namespace="notifications")),
    path("home/", include(("herfeei.home.urls", "home"), namespace="home")),
    path("orders/", include(("herfeei.orders.urls", "orders"), namespace="orders")),
    path("experts/", include(("herfeei.experts.urls", "experts"), namespace="experts")),
    # path("comments/", include(("herfeei.comments.urls", "comments"), namespace="comments")),
    # path("discounts/", include(("herfeei.discounts.urls", "discounts"), namespace="discounts")),
]
