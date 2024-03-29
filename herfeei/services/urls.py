from django.urls import include, path

from herfeei.services.apis.locations import GetCitiesView, GetProvincesView
from herfeei.services.apis.services import (GetChildrenServiceCategoryView,
                                            GetServiceCategoryView,
                                            ServiceQuestionView, ServiceView,
                                            UserAnswerView)

urlpatterns = [
    path("answers/", UserAnswerView.as_view(), name="user-answers"),
    path("<str:slug>/", ServiceView.as_view(), name="get-services"),
    path("<str:slug>/questions/",
         ServiceQuestionView.as_view(),
         name="get-service-questions"),
    path("categories/",
         include([
             path("l/",
                  GetServiceCategoryView.as_view(),
                  name="get-service-categories"),
             path("<str:slug>/",
                  GetChildrenServiceCategoryView.as_view(),
                  name="get-children-service-categories"),
         ]),
         name="categories"),
    path("locations/",
         include([
             path("p/", GetProvincesView.as_view(), name="get-provinces"),
             path("<str:slug>/", GetCitiesView.as_view(), name="get-cities"),
         ]),
         name="locations"),
]
