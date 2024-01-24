from herfeei.users.models import BaseUser, Profile


def get_profile(user: BaseUser) -> Profile:
    return Profile.objects.filter(user=user).first()
