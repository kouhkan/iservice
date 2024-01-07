from typing import List

from django.db.models import QuerySet

from herfeei.users.models import BaseUser, Address


def get_user_addresses(*, user: BaseUser) -> List[QuerySet[Address]]:
    return Address.objects.filter(user=user)


def get_user_address(*, user: BaseUser, address_id: int) -> QuerySet[Address]:
    return Address.objects.filter(user=user, id=address_id).first()
