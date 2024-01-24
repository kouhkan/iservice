from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.api.mixins import ApiAuthMixin
from herfeei.experts.models import Bookmark, Expert
from herfeei.orders.selectors.experts import (get_bookmarked_experts,
                                              get_most_rated_experts)


class BookmarkExpertsView(ApiAuthMixin, APIView):

    class OutputBookmarkExpertsSerializer(serializers.ModelSerializer):

        class Meta:
            model = Bookmark
            fields = ("expert", )
            depth = 1

    @extend_schema(responses=OutputBookmarkExpertsSerializer)
    def get(self, request):
        return Response(
            self.OutputBookmarkExpertsSerializer(
                get_bookmarked_experts(user=request.user), many=True).data)


class MostRatedExpertsView(ApiAuthMixin, APIView):

    class OutputMostRatedExpertsView(serializers.ModelSerializer):

        class Meta:
            model = Expert
            fields = ("user", "skills", "province", "city", "license",
                      "bad_background")

    @extend_schema(responses=OutputMostRatedExpertsView)
    def get(self, request, category_slug):
        return Response(
            self.OutputMostRatedExpertsView(
                get_most_rated_experts(service_category_slug=category_slug),
                many=True).data)
