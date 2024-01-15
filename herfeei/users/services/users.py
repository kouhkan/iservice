from django.db import transaction

from herfeei.users.models import BaseUser, Profile, UserAvatar


def create_profile(*, user: BaseUser, ) -> Profile:
    return Profile.objects.create(user=user)


def create_user(*, username: str) -> BaseUser:
    return BaseUser.objects.get_or_create(
        username=username, defaults={"username": username}
    )


@transaction.atomic
def register(*, username: str) -> BaseUser:
    user, created = create_user(username=username)
    if created:
        create_profile(user=user)
    return user


def get_user_avatar_image(*, img_id: int) -> UserAvatar:
    return UserAvatar.objects.filter(id=img_id, type=UserAvatar.AvatarType.USER).first()
