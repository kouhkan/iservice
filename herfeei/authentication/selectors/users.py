from herfeei.users.models import BaseUser


def get_user_by_username(*, username: str) -> BaseUser:
    return BaseUser.objects.filter(username=username).first()


def get_user_by_email(*, email: str) -> BaseUser:
    return BaseUser.objects.filter(email=email).first()
