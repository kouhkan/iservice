from datetime import timedelta

from django.core.files.storage import default_storage
from drf_spectacular.utils import extend_schema
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.api.mixins import ApiAuthMixin
from herfeei.users.models import Profile
from herfeei.users.selectors.profile import get_profile


class ProfileView(ApiAuthMixin, APIView):
    class OutPutSerializer(serializers.ModelSerializer):
        avatar_url = serializers.SerializerMethodField("secure_image_url")

        class Meta:
            model = Profile
            fields = ("user", "full_name", "city", "date_of_birth", "avatar_url", "gender")

        def secure_image_url(self, obj):
            if not (avatar_key := obj.avatar.name):
                return None
            expires_in = timedelta(hours=1)
            params = default_storage.get_object_parameters(avatar_key)
            return default_storage.url(avatar_key, params, expire=expires_in.total_seconds())

    @extend_schema(responses=OutPutSerializer)
    def get(self, request):
        query = get_profile(user=request.user)
        return Response(self.OutPutSerializer(query, context={"request": request}).data)
