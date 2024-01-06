from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.views import APIView, Response
from rest_framework_simplejwt.tokens import RefreshToken

from herfeei.authentication.tasks import send_sms
from herfeei.authentication.utils.redis_layer import get_auth_prepration_wait_time, prepare_authentication_token, \
    check_authentication_token, cleanup_token
from herfeei.users.models import BaseUser
from herfeei.users.services.users import register


class LoginByUsernameView(APIView):
    class InputLoginSerializer(serializers.Serializer):
        username = serializers.CharField(min_length=10, max_length=10)

    @extend_schema(request=InputLoginSerializer)
    def post(self, request):
        serializer = self.InputLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if wait_time := get_auth_prepration_wait_time(serializer.validated_data.get("username")):
            return Response(
                f"{wait_time} second(s) left to get a new token",
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        token = prepare_authentication_token(auth_key=serializer.validated_data.get("username"))
        send_sms(serializer.validated_data.get("username"), token)
        return Response(status=status.HTTP_204_NO_CONTENT)


class VerifyAuthenticationView(APIView):
    class InputVerifyAuthenticationSerializer(serializers.Serializer):
        username = serializers.CharField(min_length=10, max_length=10)
        token = serializers.CharField(min_length=6, max_length=6)

    class OutputVerifyAuthenticationSerializer(serializers.ModelSerializer):
        token = serializers.SerializerMethodField("get_token")

        def get_token(self, user):
            data = {}
            token_class = RefreshToken

            refresh = token_class.for_user(user)

            data["refresh"] = str(refresh)
            data["access"] = str(refresh.access_token)
            return data

        class Meta:
            model = BaseUser
            fields = ("username", "token", "role", "created_at")

    @extend_schema(request=InputVerifyAuthenticationSerializer, responses=OutputVerifyAuthenticationSerializer)
    def post(self, request):
        serializer = self.InputVerifyAuthenticationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not check_authentication_token(auth_key=serializer.validated_data.get("username"),
                                          token=serializer.validated_data.get("token")):
            return Response("Token is invalid", status=status.HTTP_400_BAD_REQUEST)

        try:
            user = register(username=serializer.validated_data.get("username"))
            cleanup_token(serializer.validated_data.get("username"))
        except Exception as ex:
            return Response(
                f"Database Error {ex}",
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(self.OutputVerifyAuthenticationSerializer(user, context={"request": request}).data)
