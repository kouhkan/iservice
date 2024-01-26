from typing import List

from django.db.models import QuerySet

from herfeei.medias.models import Media
from herfeei.users.models import BaseUser


def get_user_medias(*, user: BaseUser) -> List[QuerySet[Media]]:
    return Media.objects.filter(user=user)
