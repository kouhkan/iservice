from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.dashboards.models import Faq, FaqCategory
from herfeei.dashboards.selectors.faqs import get_faqs, get_faq_categories


class FaqView(APIView):
    class OutputFaqSerializer(serializers.ModelSerializer):
        class Meta:
            model = Faq
            fields = (
                "id", "title", "slug",
                "details", "category", "created_at"
            )

    @extend_schema(responses=OutputFaqSerializer)
    def get(self, request, slug):
        return Response(self.OutputFaqSerializer(get_faqs(slug_category=slug), many=True).data)


class FaqCategoriesView(APIView):
    class OutputFaqCategoriesSerializer(serializers.ModelSerializer):
        class Meta:
            model = FaqCategory
            fields = ("id", "title", "slug", "icon", "created_at")

    @extend_schema(responses=OutputFaqCategoriesSerializer)
    def get(self, request):
        return Response(self.OutputFaqCategoriesSerializer(get_faq_categories(), many=True).data)
