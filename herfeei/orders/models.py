from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from herfeei.common.models import BaseModel


def generate_track_token() -> str:
    return f"{uuid4().int}"[:6]


class Order(BaseModel):
    user_answer = models.ForeignKey("services.UserAnswer", on_delete=models.CASCADE, related_name="order")
    description = models.CharField(max_length=2000, null=True, blank=True)
    for_other = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="orders", null=True,
                                  blank=True)
    discount = models.ForeignKey("discounts.Discount", on_delete=models.SET_NULL, related_name="orders", null=True,
                                 blank=True)
    expert = models.ForeignKey("experts.Expert", on_delete=models.PROTECT, related_name="orders", null=True, blank=True)
    service = models.ForeignKey("services.Service", on_delete=models.PROTECT, related_name="orders", null=True,
                                blank=True)
    order_date_time = models.ManyToManyField("OrderDateTime")
    now = models.DateTimeField(default=timezone.now, null=True, blank=True)
    order_track_id = models.CharField(max_length=10, default=generate_track_token, unique=True, db_index=True,
                                      null=True, blank=True)
    is_complete = models.BooleanField(default=False)
    email_order = models.BooleanField(default=False)
    user_address = models.ForeignKey("users.Address", on_delete=models.PROTECT, related_name="orders", null=True,
                                     blank=True)

    def __str__(self):
        return f"{self.user_answer.user}"


class OrderDateTime(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()

    def __str__(self):
        return f"{self.start_time} | {self.end_time} -> {self.date}"
