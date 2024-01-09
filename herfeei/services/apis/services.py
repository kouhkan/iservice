from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.services.models import ServiceCategory
from herfeei.services.selectors.services import get_service_categories, get_children_service_category


class GetServiceCategoryView(APIView):
    class OutputGetServiceCategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = ServiceCategory
            # fields = ("title", "slug", "description", "created_at")
            fields = "__all__"

    def get(self, request):
        return Response(self.OutputGetServiceCategorySerializer(get_service_categories(), many=True).data)


class GetChildrenServiceCategoryView(APIView):
    class OutputGetChildrenServiceCategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = ServiceCategory
            # fields = ("title", "slug", "description", "created_at")
            fields = "__all__"

    def get(self, request, slug):
        if not (data := get_children_service_category(slug=slug)):
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(
            self.OutputGetChildrenServiceCategorySerializer(data, many=True).data
        )
