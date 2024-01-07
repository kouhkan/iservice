from django.db import transaction
from django.utils.text import slugify

from herfeei.users.models import BaseUser, Address


@transaction.atomic
def create_address(*, user: BaseUser, title: str, details: str, default: bool = False, phone: str = None,
                   lat: float = None, long: float = None) -> Address:
    return Address.objects.create(user=user, title=title, slug=slugify(title), details=details, default=default,
                                  phone=phone, lat=lat, long=long)


def update_address(*, user: BaseUser, address_id: int, **kwargs) -> bool:
    if not (address := Address.objects.filter(user=user, id=address_id).first()):
        return False

    for key, value in kwargs.items():
        if key == "title":
            address.slug = slugify(value)
        address.__setattr__(key, value)
    address.save()

    return address


def delete_address(*, user: BaseUser, address_id: int) -> bool:
    if not (address := Address.objects.filter(user=user, id=address_id).first()):
        return False
    address.delete()

    return True


def change_default_address(*, user: BaseUser, address_id: int) -> bool:
    if not (address := Address.objects.filter(user=user, id=address_id).first()):
        return False

    Address.objects.filter(user=user).update(default=False)
    address.default = True
    address.save()
    return address
