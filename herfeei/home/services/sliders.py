from typing import List

from django.db.models import QuerySet

from herfeei.home.models import Slider


def get_sliders() -> List[QuerySet[Slider]]:
    return Slider.objects.filter(status=True)
