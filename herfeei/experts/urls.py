from django.urls import path

from herfeei.experts.apis.experts import ExpertProfileView

urlpatterns = [
    path("<str:expert_code>/profile/",
         ExpertProfileView.as_view(),
         name="expert-profile"),
]
