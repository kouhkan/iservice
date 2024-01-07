from typing import List

from django.db.models import QuerySet

from herfeei.dashboards.models import Rule


def get_rules() -> List[QuerySet[Rule]]:
    return Rule.objects.filter(enable=True)
