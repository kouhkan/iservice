from typing import List

from django.db.models import QuerySet

from herfeei.dashboards.models import Contact


def get_contacts() -> List[QuerySet[Contact]]:
    return Contact.objects.all()
