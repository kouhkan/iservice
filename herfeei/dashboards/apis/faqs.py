from django.urls import reverse
from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.dashboards.models import Faq, FaqCategory
from herfeei.dashboards.selectors.faqs import (get_faq, get_faq_categories,
                                               get_faqs)


class FaqView(APIView):

    class FaqFilterSerializer(serializers.Serializer):
        slug = serializers.SlugField(max_length=32, required=False)
        keyword = serializers.CharField(min_length=2,
                                        max_length=64,
                                        required=False)

    class OutputFaqSerializer(serializers.ModelSerializer):

        class Meta:
            model = Faq
            fields = ("id", "title", "slug", "details", "category",
                      "created_at")

    @staticmethod
    def apply_filters(queryset, filters):
        if filters.get("slug"):
            queryset = queryset.filter(category__slug=filters["slug"])
        if filters.get("keyword"):
            queryset = queryset.filter(details__icontains=filters["keyword"])
        return queryset

    @extend_schema(request=FaqFilterSerializer, responses=OutputFaqSerializer)
    def get(self, request):
        filter_serializer = self.FaqFilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)
        queryset = get_faqs()
        queryset = self.apply_filters(queryset,
                                      filter_serializer.validated_data)
        return Response(self.OutputFaqSerializer(queryset, many=True).data)


class FaqDetailView(APIView):

    class OutputFaqSerializer(serializers.ModelSerializer):

        class Meta:
            model = Faq
            fields = ("id", "title", "slug", "details", "category",
                      "created_at")

    @extend_schema(responses=OutputFaqSerializer)
    def get(self, request, slug):
        if not (faq := get_faq(slug=slug)):
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(self.OutputFaqSerializer(faq).data)


class FaqCategoriesView(APIView):

    class OutputFaqCategoriesSerializer(serializers.ModelSerializer):

        class Meta:
            model = FaqCategory
            fields = ("id", "title", "slug", "icon", "created_at")

    @extend_schema(responses=OutputFaqCategoriesSerializer)
    def get(self, request):
        return Response(
            self.OutputFaqCategoriesSerializer(get_faq_categories(),
                                               many=True).data)
