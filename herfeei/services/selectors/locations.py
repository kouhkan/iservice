from typing import List

from django.db.models import QuerySet

from herfeei.services.models import Province, City


def get_provinces() -> List[QuerySet[Province]]:
    return Province.objects.all()


def get_cities(*, province_slug: str) -> List[QuerySet[City]]:
    return City.objects.filter(province__slug=province_slug)
