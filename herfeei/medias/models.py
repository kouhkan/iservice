from django.contrib.auth import get_user_model
from django.db import models

from herfeei.common.models import BaseModel


class Media(BaseModel):
    class BucketName(models.TextChoices):
        IMAGE = "image"
        VIDEO = "video"

    class MediaType(models.TextChoices):
        VIDEO = "VIDEO"
        IMAGE = "IMAGE"

    class MediaUsage(models.TextChoices):
        ADMIN_AVATAR = 0
        EXPERT_AVATAR = 1
        USER_AVATAR = 2
        ADMIN = 3
        SERVICE = 4
        ORDER = 5

    user = models.ForeignKey(get_user_model(),
                             on_delete=models.PROTECT,
                             related_name="medias",
                             null=True,
                             blank=True)
    bucket_name = models.CharField(max_length=32,
                                   choices=BucketName.choices,
                                   default=BucketName.IMAGE)
    file = models.CharField(max_length=1024,
                            db_index=True,
                            null=True,
                            blank=True)
    _file = models.FileField(upload_to="admin/",
                             null=True,
                             blank=True)
    extra = models.JSONField(null=True,
                             blank=True)
    type = models.CharField(max_length=5,
                            choices=MediaType.choices,
                            default=MediaType.IMAGE)
    illegal = models.BooleanField(default=False)
    usage = models.CharField(max_length=1,
                             choices=MediaUsage.choices,
                             default=MediaUsage.USER_AVATAR)

    def __str__(self):
        return f"{self.file}" or f"{self._file}"
