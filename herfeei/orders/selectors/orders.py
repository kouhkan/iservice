from datetime import timedelta
from typing import List

from django.db.models import QuerySet
from django.utils import timezone

from herfeei.orders.models import Order


def get_incomplete_user_orders(*, time_passed: int = 6) -> List[QuerySet[Order]]:
    return Order.objects.filter(
        created_at__lte=timezone.now() - timedelta(hours=time_passed),
        is_complete=False,
        status=Order.OrderStatus.CREATED
    )
