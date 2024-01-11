from typing import List

from django.db.models import QuerySet

from herfeei.users.models import UserAvatar


def get_user_avatars() -> List[QuerySet[UserAvatar]]:
    return UserAvatar.objects.filter(type=UserAvatar.AvatarType.USER)
