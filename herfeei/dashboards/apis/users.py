from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.api.mixins import ApiAuthMixin
from herfeei.users.models import Profile


class UpdateUserProfileView(ApiAuthMixin, APIView):
    class InputUpdateProfileSerializer(serializers.Serializer):
        full_name = serializers.CharField(max_length=64, allow_null=True, allow_blank=True, required=False)
        date_of_birth = serializers.DateField(allow_null=True, required=False)
        gender = serializers.CharField(max_length=6, allow_null=True, allow_blank=True, required=False)
        city = serializers.CharField(max_length=128, allow_null=True, allow_blank=True, required=False)
        email = serializers.EmailField(max_length=128, allow_null=True, allow_blank=True, required=False)
        username = serializers.CharField(min_length=10, max_length=10, allow_null=True, allow_blank=True, required=False)

    class OutputUpdateProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = ("full_name", "date_of_birth", "gender", "city", "avatar")

    @extend_schema(request=InputUpdateProfileSerializer, responses=OutputUpdateProfileSerializer)
    def patch(self, request):
        serializer = self.InputUpdateProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            request.user.profile.full_name = serializer.validated_data.get("full_name", request.user.profile.full_name)
            request.user.profile.gender = serializer.validated_data.get("gender", request.user.profile.gender)
            request.user.profile.city = serializer.validated_data.get("city", request.user.profile.city)
            request.user.profile.date_of_birth = serializer.validated_data.get("date_of_birth",
                                                                               request.user.profile.date_of_birth)
            request.user.email = serializer.validated_data.get("email", request.user.email)
            request.user.username = serializer.validated_data.get("username", request.user.username)
            request.user.save()
            return Response(self.OutputUpdateProfileSerializer(request.user.profile).data, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(f"{ex}", status=status.HTTP_400_BAD_REQUEST)


class UpdateUserAvatarView(ApiAuthMixin, APIView):
    class InputUserAvatarSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = ("avatar",)

    class OutputUserAvatarSerializer(serializers.ModelSerializer):
        avatar_url = serializers.SerializerMethodField("get_avatar_url")

        class Meta:
            model = Profile
            fields = ("avatar_url", "full_name", "gender", "date_of_birth")

        def get_avatar_url(self, obj):
            if obj.avatar:
                request = self.context.get("request")

                if request:
                    return request.build_absolute_uri(obj.avatar.url)
            return None

    def patch(self, request):
        serializer = self.InputUserAvatarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        request.user.profile.avatar = serializer.validated_data.get("avatar", request.user.profile.avatar)
        request.user.profile.save()

        return Response(self.OutputUserAvatarSerializer(request.user.profile, context={"request": request}).data)
