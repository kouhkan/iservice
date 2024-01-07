from django.db import models

from herfeei.common.models import BaseModel


class Rule(BaseModel):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=128)
    slug = models.SlugField(max_length=32, unique=True, allow_unicode=True, db_index=True)
    details = models.TextField()
    enable = models.BooleanField(default=True)

    def __str__(self):
        return self.title


