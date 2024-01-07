from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.api.mixins import ApiAuthMixin
from herfeei.users.models import Address
from herfeei.users.selectors.addresses import get_user_addresses, get_user_address
from herfeei.users.services.addresses import create_address


class CreateUserAddressView(ApiAuthMixin, APIView):
    class InputUserAddressSerializer(serializers.Serializer):
        title = serializers.CharField(min_length=2, max_length=64)
        details = serializers.CharField(min_length=8, max_length=512)
        phone = serializers.CharField(min_length=10, max_length=10, required=False, allow_null=True)
        default = serializers.BooleanField(default=False)
        lat = serializers.DecimalField(max_digits=9, decimal_places=6, required=False, allow_null=True)
        long = serializers.DecimalField(max_digits=9, decimal_places=6, required=False, allow_null=True)

    class OutputUserAddressSerializer(serializers.ModelSerializer):
        class Meta:
            model = Address
            fields = (
                "id", "user", "title",
                "slug", "details", "phone",
                "default", "lat", "long",
                "created_at", "updated_at"
            )

    @extend_schema(request=InputUserAddressSerializer, responses=OutputUserAddressSerializer)
    def post(self, request):
        serializer = self.InputUserAddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            address = create_address(
                user=request.user, title=serializer.validated_data.get("title"),
                details=serializer.validated_data.get("details"),
                default=serializer.validated_data.get("default"),
                lat=serializer.validated_data.get("lat"),
                long=serializer.validated_data.get("long"),
                phone=serializer.validated_data.get("phone"),
            )
            return Response(self.OutputUserAddressSerializer(address).data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response(f"Error -> {ex}", status=status.HTTP_400_BAD_REQUEST)


class GetUserAddressesListView(ApiAuthMixin, APIView):
    class OutputUserAddressesListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Address
            fields = (
                "id", "user", "title",
                "slug", "details", "phone",
                "default", "lat", "long",
                "created_at", "updated_at"
            )

    def get(self, request):
        addresses = get_user_addresses(user=request.user)
        return Response(self.OutputUserAddressesListSerializer(addresses, many=True).data)


class GetUserAddressView(ApiAuthMixin, APIView):
    class OutputUserAddressSerializer(serializers.ModelSerializer):
        class Meta:
            model = Address
            fields = (
                "id", "user", "title",
                "slug", "details", "phone",
                "default", "lat", "long",
                "created_at", "updated_at"
            )

    def get(self, request, id):
        address = get_user_address(user=request.user, address_id=id)
        if not address:
            return Response(data={"message": "invalid id"}, status=status.HTTP_404_NOT_FOUND)
        return Response(self.OutputUserAddressSerializer(address).data)
