from herfeei.users.models import BaseUser, Profile


def for_other(*, username: str, full_name: str) -> BaseUser:
    user, created = BaseUser.objects.get_or_create(
        username=username, defaults={"username": username})
    if created:
        Profile.objects.create(user=user, full_name=full_name)
    return user
