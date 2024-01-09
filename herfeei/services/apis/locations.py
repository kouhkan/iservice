from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.services.models import Province
from herfeei.services.selectors.locations import get_provinces


class GetProvincesView(APIView):
    class OutputGetProvincesSerializer(serializers.ModelSerializer):
        class Meta:
            model = Province
            fields = ("name", "slug", "city")
            depth = 1

    @extend_schema(responses=OutputGetProvincesSerializer)
    def get(self, request):
        return Response(self.OutputGetProvincesSerializer(get_provinces(), many=True).data)
