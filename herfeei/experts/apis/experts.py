from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.api.mixins import ApiAuthMixin
from herfeei.experts.selectors.experts import (get_expert, get_expert_comments,
                                               get_expert_comments_count,
                                               get_expert_complete_orders,
                                               get_expert_rate,
                                               get_expert_samples)
from herfeei.experts.serializers.serializers import (
    OutputExpertCommentsSerializer, OutputExpertSerializer,
    OutputSampleExpertSerializer)


class ExpertProfileView(ApiAuthMixin, APIView):

    class OutputExpertProfileSerializer(serializers.Serializer):
        comments = OutputExpertCommentsSerializer(many=True)
        samples = OutputSampleExpertSerializer(many=True)
        expert = OutputExpertSerializer()
        comment_count = serializers.IntegerField()
        expert_rate = serializers.FloatField(min_value=0, max_value=5)
        complete_order = serializers.IntegerField()

    def get(self, request, expert_code):
        data = {}
        data["expert"] = get_expert(expert_code=expert_code)
        data["expert_rate"] = get_expert_rate(expert_code=expert_code)
        data["comments"] = get_expert_comments(expert_code=expert_code)
        data["comment_count"] = get_expert_comments_count(
            expert_code=expert_code)
        data["complete_order"] = get_expert_complete_orders(
            expert_code=expert_code)
        data["samples"] = get_expert_samples(expert_code=expert_code)
        serializer = self.OutputExpertProfileSerializer(data)
        return Response(serializer.data)
