from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.home.models import Slider
from herfeei.home.services.sliders import get_sliders


class SliderView(APIView):
    class OutputSlidersSerializer(serializers.ModelSerializer):
        class Meta:
            model = Slider
            fields = ("title", "slug", "caption", "description", "image", "status", "weight")

    @extend_schema(responses=OutputSlidersSerializer)
    def get(self, request):
        return Response(self.OutputSlidersSerializer(get_sliders(), many=True).data)
