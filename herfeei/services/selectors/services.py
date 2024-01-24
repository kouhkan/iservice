from typing import List

from django.db.models import QuerySet

from herfeei.services.models import Question, Service, ServiceCategory


def get_service_categories() -> List[QuerySet[ServiceCategory]]:
    return ServiceCategory.objects.filter(is_public=True)


def get_service_category(*, slug: str) -> QuerySet[ServiceCategory]:
    return ServiceCategory.objects.filter(is_public=True, slug=slug).first()


def get_children_service_category(
        *, slug: str) -> List[QuerySet[ServiceCategory]]:
    return ServiceCategory.objects.filter(is_public=True, slug=slug).first().get_children() \
        if ServiceCategory.objects.filter(is_public=True, slug=slug).first() \
        else None


def get_service(*, service_category_slug: str) -> QuerySet[Service]:
    return Service.objects.filter(category__slug=service_category_slug).first()


def get_service_questions(
        *, service_category_slug: str) -> List[QuerySet[Question]]:
    return Question.objects.filter(category__slug=service_category_slug)
