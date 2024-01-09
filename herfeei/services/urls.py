from django.urls import path, include

from herfeei.services.apis.locations import GetProvincesView
from herfeei.services.apis.services import GetServiceCategoryView

urlpatterns = [
    path("categories/", GetServiceCategoryView.as_view(), name="get-service-categories"),

    path("locations/", include([
        path("", GetProvincesView.as_view(), name="get-provinces"),
    ]), name="locations"),
]