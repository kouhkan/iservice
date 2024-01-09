from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.services.models import ServiceCategory, Service
from herfeei.services.selectors.services import get_service_categories, get_children_service_category, get_service


class GetServiceCategoryView(APIView):
    class OutputGetServiceCategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = ServiceCategory
            # fields = ("title", "slug", "description", "created_at")
            fields = "__all__"

    @extend_schema(responses=OutputGetServiceCategorySerializer)
    def get(self, request):
        return Response(self.OutputGetServiceCategorySerializer(get_service_categories(), many=True).data)


class GetChildrenServiceCategoryView(APIView):
    class OutputGetChildrenServiceCategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = ServiceCategory
            # fields = ("title", "slug", "description", "created_at")
            fields = "__all__"

    @extend_schema(responses=OutputGetChildrenServiceCategorySerializer)
    def get(self, request, slug):
        if not (data := get_children_service_category(slug=slug)):
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(
            self.OutputGetChildrenServiceCategorySerializer(data, many=True).data
        )


class ServiceView(APIView):
    class OutputServiceSerializer(serializers.ModelSerializer):
        class Meta:
            model = Service
            fields = "__all__"
            depth = 1

    @extend_schema(responses=OutputServiceSerializer)
    def get(self, request, slug):
        return Response(
            self.OutputServiceSerializer(get_service(service_category_slug=slug)).data
        )
