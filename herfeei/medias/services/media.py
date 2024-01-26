from herfeei.medias.models import Media
from herfeei.users.models import BaseUser


def create_media(*,
                 file_name: str,
                 user: BaseUser = None,
                 bucket_name: str = "image",
                 extra: dict = None,
                 type: str = Media.MediaType.IMAGE,
                 usage: str = Media.MediaUsage.ORDER
                 ) -> Media:
    return Media.objects.create(
        user=user,
        file=file_name,
        bucket_name=bucket_name,
        extra=extra,
        type=type,
        usage=usage
    )
