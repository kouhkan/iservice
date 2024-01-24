from datetime import timedelta

from django.core.files.storage import default_storage
from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.api.mixins import ApiAuthMixin
from herfeei.users.models import Profile, UserAvatar
from herfeei.users.services.users import get_user_avatar_image


class UpdateUserProfileView(ApiAuthMixin, APIView):

    class InputUpdateProfileSerializer(serializers.Serializer):
        full_name = serializers.CharField(max_length=64,
                                          allow_null=True,
                                          allow_blank=True,
                                          required=False)
        date_of_birth = serializers.DateField(allow_null=True, required=False)
        gender = serializers.CharField(max_length=6,
                                       allow_null=True,
                                       allow_blank=True,
                                       required=False)
        city = serializers.CharField(max_length=128,
                                     allow_null=True,
                                     allow_blank=True,
                                     required=False)
        email = serializers.EmailField(max_length=128,
                                       allow_null=True,
                                       allow_blank=True,
                                       required=False)
        username = serializers.CharField(min_length=10,
                                         max_length=10,
                                         allow_null=True,
                                         allow_blank=True,
                                         required=False)

    class OutputUpdateProfileSerializer(serializers.ModelSerializer):
        avatar_url = serializers.SerializerMethodField("secure_image_url")

        class Meta:
            model = Profile
            fields = ("user", "full_name", "city", "date_of_birth",
                      "avatar_url", "gender")

        def secure_image_url(self, obj):
            if not obj.avatar:
                return None

            if not (avatar_key := obj.avatar.title):
                return None
            expires_in = timedelta(hours=1)
            params = default_storage.get_object_parameters(avatar_key)
            return default_storage.url(avatar_key,
                                       params,
                                       expire=expires_in.total_seconds())

    @extend_schema(request=InputUpdateProfileSerializer,
                   responses=OutputUpdateProfileSerializer)
    def patch(self, request):
        serializer = self.InputUpdateProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            request.user.profile.full_name = serializer.validated_data.get(
                "full_name", request.user.profile.full_name)
            request.user.profile.gender = serializer.validated_data.get(
                "gender", request.user.profile.gender)
            request.user.profile.city = serializer.validated_data.get(
                "city", request.user.profile.city)
            request.user.profile.date_of_birth = serializer.validated_data.get(
                "date_of_birth", request.user.profile.date_of_birth)
            request.user.email = serializer.validated_data.get(
                "email", request.user.email)
            request.user.username = serializer.validated_data.get(
                "username", request.user.username)
            request.user.save()
            return Response(self.OutputUpdateProfileSerializer(
                request.user.profile).data,
                            status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(f"{ex}", status=status.HTTP_400_BAD_REQUEST)


class UpdateUserAvatarView(ApiAuthMixin, APIView):

    class InputUserAvatarSerializer(serializers.Serializer):
        img_id = serializers.IntegerField()

    class OutputUserAvatarSerializer(serializers.ModelSerializer):

        class AvatarSerializer(serializers.ModelSerializer):

            class Meta:
                model = UserAvatar
                fields = ("title", "slug", "avatar")

        avatar = AvatarSerializer(read_only=True)

        class Meta:
            model = Profile
            fields = ("user", "full_name", "city", "date_of_birth", "avatar",
                      "gender")

    def patch(self, request):
        serializer = self.InputUserAvatarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not (avatar := get_user_avatar_image(
                img_id=serializer.validated_data.get("img_id"))):
            return Response({"msg": "invalid avatar"},
                            status=status.HTTP_400_BAD_REQUEST)
        request.user.profile.avatar = avatar
        request.user.profile.save()

        return Response(
            self.OutputUserAvatarSerializer(request.user.profile,
                                            context={
                                                "request": request
                                            }).data)
