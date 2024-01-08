from typing import List

from django.db.models import QuerySet

from herfeei.dashboards.models import Faq, FaqCategory


def get_faq_categories() -> List[QuerySet[FaqCategory]]:
    return FaqCategory.objects.filter(status=True)


def get_faqs() -> List[QuerySet[Faq]]:
    return Faq.objects.filter(status=True)


def get_faq(*, slug: str) -> QuerySet[Faq]:
    return Faq.objects.filter(status=True, slug=slug).first()
