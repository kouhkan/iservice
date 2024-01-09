from django.urls import path

from herfeei.services.apis.services import GetServiceCategoryView

urlpatterns = [
    path("categories/", GetServiceCategoryView.as_view(), name="get-service-categories"),
]