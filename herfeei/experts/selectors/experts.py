from typing import List

from django.db.models import QuerySet, Q

from herfeei.experts.models import Expert
from herfeei.orders.models import Order


def get_available_experts(*, order: Order) -> List[QuerySet[Expert]]:
    suggested_experts = Expert.objects.filter(
        status=Expert.ExpertStatus.ACTIVE,
        skills__category__slug=order.service.category.slug,
    )

    for order_date_time in order.order_date_time.all():
        start_time = order_date_time.start_time
        end_time = order_date_time.end_time
        date = order_date_time.date
        print(start_time, end_time, date)

        suggested_experts = suggested_experts.filter(
            Q(available__start_time__lte=start_time, available__end_time__gte=end_time) &
            Q(available__date=date)
        )

    # Remove experts that they are busy
    suggested_experts = suggested_experts.exclude(
        orders__order_date_time__in=order.order_date_time.all()
    )

    return suggested_experts
