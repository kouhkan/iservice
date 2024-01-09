from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.services.models import ServiceCategory
from herfeei.services.selectors.services import get_service_categories


class GetServiceCategoryView(APIView):
    class OutputGetServiceCategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = ServiceCategory
            # fields = ("title", "slug", "description", "created_at")
            fields = "__all__"

    def get(self, request):
        return Response(self.OutputGetServiceCategorySerializer(get_service_categories(), many=True).data)
