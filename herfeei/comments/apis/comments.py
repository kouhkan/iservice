from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.api.mixins import ApiAuthMixin
from herfeei.comments.models import Comment
from herfeei.comments.services.comments import create_comment


class CreateCommentView(ApiAuthMixin, APIView):
    class InputCommentSerializer(serializers.Serializer):
        rate = serializers.IntegerField(min_value=1, max_value=5)
        description = serializers.CharField(min_length=2, max_length=512)
        order_track_id = serializers.CharField(min_length=6, max_length=10)

    class OutputCommentSerializer(serializers.ModelSerializer):
        user = serializers.SerializerMethodField("get_user")

        def get_user(self, obj):
            data = {}
            data["full_name"] = obj.profile.full_name
            return data

        class Meta:
            model = Comment
            fields = ("user", "rate", "description", "created_at")

    def post(self, request):
        serializer = self.InputCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if not (comment := create_comment(**serializer.validated_data)):
            return Response({"msg": "order is not complete"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(self.OutputCommentSerializer(comment).data, status=status.HTTP_201_CREATED)
       