from drf_spectacular.utils import extend_schema
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from herfeei.api.mixins import ApiAuthMixin
from herfeei.services.models import (Question, Service, ServiceCategory,
                                     UserAnswer)
from herfeei.services.selectors.services import (get_children_service_category,
                                                 get_service,
                                                 get_service_categories,
                                                 get_service_questions)
from herfeei.services.services.services import create_user_answers


class GetServiceCategoryView(APIView):

    class OutputGetServiceCategorySerializer(serializers.ModelSerializer):

        class Meta:
            model = ServiceCategory
            # fields = ("title", "slug", "description", "created_at")
            fields = "__all__"

    @extend_schema(responses=OutputGetServiceCategorySerializer)
    def get(self, request):
        return Response(
            self.OutputGetServiceCategorySerializer(get_service_categories(),
                                                    many=True).data)


class GetChildrenServiceCategoryView(APIView):

    class OutputGetChildrenServiceCategorySerializer(
            serializers.ModelSerializer):

        class Meta:
            model = ServiceCategory
            # fields = ("title", "slug", "description", "created_at")
            fields = "__all__"

    @extend_schema(responses=OutputGetChildrenServiceCategorySerializer)
    def get(self, request, slug):
        if not (data := get_children_service_category(slug=slug)):
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(
            self.OutputGetChildrenServiceCategorySerializer(data,
                                                            many=True).data)


class ServiceView(APIView):

    class OutputServiceSerializer(serializers.ModelSerializer):

        class Meta:
            model = Service
            fields = "__all__"
            depth = 1

    @extend_schema(responses=OutputServiceSerializer)
    def get(self, request, slug):
        return Response(
            self.OutputServiceSerializer(
                get_service(service_category_slug=slug)).data)


class ServiceQuestionView(APIView):

    class OutputServiceQuestionSerializer(serializers.ModelSerializer):

        class Meta:
            model = Question
            fields = ("title", "slug", "category", "items")
            depth = 2

    @extend_schema(responses=OutputServiceQuestionSerializer)
    def get(self, request, slug):
        return Response(
            self.OutputServiceQuestionSerializer(
                get_service_questions(service_category_slug=slug),
                many=True).data)


class UserAnswerView(ApiAuthMixin, APIView):

    class InputUserAnswerSerializer(serializers.ModelSerializer):

        class Meta:
            model = UserAnswer
            fields = ("answers", )

    class OutputUserAnswerSerializer(serializers.ModelSerializer):

        class Meta:
            model = UserAnswer
            fields = ("user", "answers", "created_at")

    @extend_schema(request=InputUserAnswerSerializer,
                   responses=OutputUserAnswerSerializer)
    def post(self, request):
        serializer = self.InputUserAnswerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            self.OutputUserAnswerSerializer(
                create_user_answers(
                    user=request.user,
                    answers=serializer.validated_data.get("answers"))).data)
