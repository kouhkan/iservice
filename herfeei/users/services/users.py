from django.db import transaction

from herfeei.users.models import BaseUser, Profile


def create_profile(*, user: BaseUser, ) -> Profile:
    return Profile.objects.create(user=user)


def create_user(*, username: str) -> BaseUser:
    return BaseUser.objects.get_or_create(
        username=username, defaults={"username": username}
    )


@transaction.atomic
def register(*, username: str) -> BaseUser:
    user = create_user(username=username)
    create_profile(user=user)
    return user
