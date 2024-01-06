from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.api.mixins import ApiAuthMixin
from herfeei.users.models import Profile
from herfeei.users.selectors.profile import get_profile


class ProfileView(ApiAuthMixin, APIView):
    class OutPutSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = ("user", "full_name", "city", "date_of_birth", "avatar", "gender")

    @extend_schema(responses=OutPutSerializer)
    def get(self, request):
        query = get_profile(user=request.user)
        return Response(self.OutPutSerializer(query, context={"request": request}).data)
