from datetime import datetime
from typing import List

from django.db.models import QuerySet

from herfeei.discounts.models import Discount
from herfeei.experts.models import Expert
from herfeei.orders.models import Order, OrderDateTime
from herfeei.orders.selectors.order_for_other import for_other_order
from herfeei.services.models import Service, UserAnswer
from herfeei.users.models import Address


def create_order(*,
                 user_answer: UserAnswer,
                 description: str | None,
                 for_other: dict | None,
                 order_date_time: OrderDateTime,
                 expert: Expert,
                 discount: Discount | None,
                 service: Service,
                 now: datetime | None,
                 email_order: bool = False,
                 user_address: Address) -> Order:
    order = Order.objects.create(user_answer=user_answer,
                                 description=description,
                                 for_other=for_other_order(**for_other) if for_other else None,
                                 discount=discount,
                                 expert=expert,
                                 service=service,
                                 now=now,
                                 email_order=email_order,
                                 user_address=user_address)
    order.order_date_time.set(order_date_time)
    return order


def change_status_notified(*, orders: List[QuerySet[Order]]) -> List[QuerySet[Order]]:
    for order in orders:
        order.status = Order.OrderStatus.NOTIFIED
    Order.objects.bulk_update(orders, ("status",))
    return orders
