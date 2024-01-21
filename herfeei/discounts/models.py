from django.db import models
from django.utils import timezone

from herfeei.common.models import BaseModel


class Discount(BaseModel):
    user = models.ForeignKey("users.BaseUser", on_delete=models.CASCADE, related_name="discounts", null=True, blank=True)
    service_category = models.ForeignKey("services.ServiceCategory", on_delete=models.CASCADE, related_name="discounts", null=True, blank=True)
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True, db_index=True, allow_unicode=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    token = models.CharField(max_length=20, unique=True, db_index=True)
    percent = models.PositiveSmallIntegerField(default=1, null=True, blank=True)
    amount = models.PositiveSmallIntegerField(null=True, blank=True)
    usage = models.PositiveSmallIntegerField(default=1, null=True, blank=True)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField()

    def __str__(self):
        return self.title

