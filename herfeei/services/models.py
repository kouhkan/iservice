from django.db import models
from treebeard.mp_tree import MP_Node

from herfeei.common.models import BaseModel


class Province(BaseModel):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True, db_index=True, allow_unicode=True)

    def __str__(self):
        return self.name


class City(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=64, unique=True, db_index=True, allow_unicode=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="city")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


class ServiceCategory(MP_Node, BaseModel):
    title = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, db_index=True, unique=True, allow_unicode=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    is_public = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.title
