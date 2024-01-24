from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.dashboards.models import Rule
from herfeei.dashboards.selectors.rules import get_rules


class GetRulesView(APIView):

    class OutputRulesSerializer(serializers.ModelSerializer):

        class Meta:
            model = Rule
            fields = ("id", "title", "subtitle", "details", "created_at",
                      "updated_at", "slug")

    def get(self, request):
        return Response(
            self.OutputRulesSerializer(get_rules(), many=True).data)
