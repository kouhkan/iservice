from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.dashboards.models import Faq
from herfeei.dashboards.selectors.faqs import get_faqs


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
