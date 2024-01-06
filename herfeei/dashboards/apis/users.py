from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.api.mixins import ApiAuthMixin
from herfeei.users.models import Profile


class UpdateUserProfileView(ApiAuthMixin, APIView):
    class InputUpdateProfileSerializer(serializers.Serializer):
        full_name = serializers.CharField(max_length=64, allow_null=True, allow_blank=True)
        date_of_birth = serializers.DateField(allow_null=True, allow_blank=True)
        gender = serializers.CharField(max_length=6, allow_null=True, allow_blank=True)
        city = serializers.CharField(max_length=128, allow_null=True, allow_blank=True)
        email = serializers.EmailField(max_length=128, allow_null=True, allow_blank=True)
        username = serializers.CharField(min_length=10, max_length=10, allow_null=True, allow_blank=True)

    class OutputUpdateProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = ("full_name", "date_of_birth", "gender", "city", "created_at")

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
            return Response("user's data updated", status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(f"{ex}", status=status.HTTP_400_BAD_REQUEST)
