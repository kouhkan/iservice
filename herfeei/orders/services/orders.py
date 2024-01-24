from datetime import datetime

from herfeei.discounts.models import Discount
from herfeei.experts.models import Expert
from herfeei.orders.models import Order, OrderDateTime
from herfeei.services.models import Service, UserAnswer
from herfeei.users.models import Address, BaseUser


def create_order(*,
                 user_answer: UserAnswer,
                 description: str | None,
                 for_other: BaseUser | None,
                 order_date_time: OrderDateTime,
                 expert: Expert,
                 discount: Discount | None,
                 service: Service,
                 now: datetime | None,
                 email_order: bool = False,
                 user_address: Address) -> Order:
    order = Order.objects.create(user_answer=user_answer,
                                 description=description,
                                 for_other=for_other,
                                 discount=discount,
                                 expert=expert,
                                 service=service,
                                 now=now,
                                 email_order=email_order,
                                 user_address=user_address)
    order.order_date_time.set(order_date_time)
    return order
