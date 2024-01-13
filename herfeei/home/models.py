from django.db import models

from herfeei.common.models import BaseModel


class Slider(BaseModel):
    title = models.CharField(max_length=64, null=True, blank=True)
    slug = models.SlugField(max_length=32, unique=True, db_index=True, allow_unicode=True)
    caption = models.CharField(max_length=64, null=True, blank=True)
    description = models.TextField()
    weight = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to="slider/")
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.slug}"

    class Meta:
        ordering = ("weight",)
