from typing import List

from django.db.models import QuerySet

from herfeei.services.models import ServiceCategory


def get_service_categories() -> List[QuerySet[ServiceCategory]]:
    return ServiceCategory.objects.filter(is_public=True)


def get_service_category(slug: str) -> QuerySet[ServiceCategory]:
    return ServiceCategory.objects.filter(is_public=True, slug=slug).first()


def get_children_service_category(slug: str) -> List[QuerySet[ServiceCategory]]:
    return ServiceCategory.objects.filter(is_public=True, slug=slug).first().get_children() \
        if ServiceCategory.objects.filter(is_public=True, slug=slug).first() \
        else None
