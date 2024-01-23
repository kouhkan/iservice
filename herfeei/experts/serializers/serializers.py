from rest_framework import serializers

from herfeei.comments.models import Comment
from herfeei.experts.models import Sample, Expert


class OutputExpertCommentsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField("get_user")

    def get_user(self, obj):
        return {"full_name": obj.profile.full_name}

    class Meta:
        model = Comment
        fields = ("user", "rate", "description", "created_at")


class OutputSampleExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ("category", "image", "description")


class OutputExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = ("expert_code", "province", "city", "license", "bad_background", "status", "created_at")
        depth = 1
