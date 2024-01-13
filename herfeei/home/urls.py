from django.urls import path

from herfeei.home.apis.sliders import SliderView

urlpatterns = [
    path("sliders/", SliderView.as_view(), name="sliders"),
]
