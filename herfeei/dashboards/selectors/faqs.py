from typing import List

from django.db.models import QuerySet

from herfeei.dashboards.models import Faq, FaqCategory


def get_faq_categories() -> List[QuerySet[FaqCategory]]:
    return FaqCategory.objects.filter(status=True)


def get_faqs(*, slug_category: str) -> List[QuerySet[Faq]]:
    return Faq.objects.filter(category__slug=slug_category, status=True)
