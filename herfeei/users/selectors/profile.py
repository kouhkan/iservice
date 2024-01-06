from herfeei.users.models import Profile, BaseUser


def get_profile(user: BaseUser) -> Profile:
    return Profile.objects.filter(user=user).first()
