from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.api.mixins import ApiAuthMixin
from herfeei.notifications.models import UserNotification
from herfeei.notifications.selectors.notifications import \
    get_user_notifications
from herfeei.notifications.services.notifications import \
    change_to_read_notification


class GetUserNotificationsView(ApiAuthMixin, APIView):

    class NotificationFilterSerializer(serializers.Serializer):
        category = serializers.SlugField(min_length=1,
                                         max_length=64,
                                         required=False)
        status = serializers.CharField(max_length=6, required=False)

    class OutputGetUserNotificationSerializer(serializers.ModelSerializer):

        class Meta:
            model = UserNotification
            fields = ("id", "notification", "options", "status", "created_at")
            depth = 1

    def apply_filter(self, queryset, filters):
        if category := filters.get("category"):
            queryset = queryset.filter(notification__category__slug=category)
        if status := (filters.get("status")):
            queryset = queryset.filter(status=status)
        return queryset

    @extend_schema(responses=OutputGetUserNotificationSerializer)
    def get(self, request):
        filter_serializer = self.NotificationFilterSerializer(
            data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)
        queryset = get_user_notifications(user=request.user)
        queryset = self.apply_filter(queryset,
                                     filter_serializer.validated_data)
        return Response(
            self.OutputGetUserNotificationSerializer(queryset, many=True).data)


class ReadUserNotificationView(ApiAuthMixin, APIView):

    def patch(self, request, id):
        if not change_to_read_notification(user=request.user,
                                           notification_id=id):
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
