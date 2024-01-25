from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.api.mixins import ApiAuthMixin
from herfeei.core.exceptions import (CompleteEmailProfileException,
                                     OrderTimeException, OwnerOfOrderException)
from herfeei.orders.models import Order
from herfeei.orders.services.orders import create_order


class UserOrderView(ApiAuthMixin, APIView):
    class InputOrderSerializer(serializers.ModelSerializer):
        class ForOtherSerializer(serializers.Serializer):
            username = serializers.CharField(min_length=10, max_length=10)
            fullname = serializers.CharField(min_length=3, max_length=64)

        for_other = ForOtherSerializer(required=False)

        class Meta:
            model = Order
            fields = ("user_answer", "description", "for_other", "discount",
                      "expert", "service", "order_date_time", "now",
                      "email_order", "user_address")

        def validate(self, attrs):
            if not attrs.get("now") and not attrs.get("order_date_time"):
                raise OrderTimeException("User must choose a date for order")

            if attrs.get("email_order"):
                if not attrs.get("user_answer").user.email:
                    raise CompleteEmailProfileException(
                        "User must set email in profile")

            if self.context.get("request").user != attrs.get(
                    "user_answer").user:
                raise OwnerOfOrderException(
                    "This order is not own of this user")

            return attrs

    class OutputOrderSerializer(serializers.ModelSerializer):

        class Meta:
            model = Order
            fields = "__all__"

    @extend_schema(request=InputOrderSerializer,
                   responses=OutputOrderSerializer)
    def post(self, request):
        serializer = self.InputOrderSerializer(data=request.data,
                                               context={"request": request})
        serializer.is_valid(raise_exception=True)
        order = create_order(
            user_answer=serializer.validated_data.get("user_answer"),
            order_date_time=serializer.validated_data.get("order_date_time"),
            service=serializer.validated_data.get("service"),
            discount=serializer.validated_data.get("discount"),
            expert=serializer.validated_data.get("expert"),
            user_address=serializer.validated_data.get("user_address"),
            now=serializer.validated_data.get("now"),
            description=serializer.validated_data.get("description"),
            email_order=serializer.validated_data.get("email_order"),
            for_other=serializer.validated_data.get("for_other"),
        )
        return Response(self.OutputOrderSerializer(order).data,
                        status=status.HTTP_201_CREATED)
