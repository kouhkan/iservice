from django.urls import path, include

from herfeei.orders.apis.experts import BookmarkExpertsView, MostRatedExpertsView
from herfeei.orders.apis.order import UserOrderView

urlpatterns = [
    path("", UserOrderView.as_view(), name="create-order"),

    path("experts/", include([
        path("bookmarks/", BookmarkExpertsView.as_view(), name="orders-bookmarked-experts"),
        path("rate/<str:category_slug>/", MostRatedExpertsView.as_view(), name="orders-rate-experts"),
    ]), name="order-experts")
]
