from herfeei.comments.models import Comment
from herfeei.orders.models import Order
from herfeei.users.models import BaseUser


def create_comment(*, user: BaseUser, order_track_id: int, rate: int,
                   description: str) -> Comment | None:
    if not (order := Order.objects.filter(user_answer__user=user,
                                          order_track_id=order_track_id,
                                          is_complete=True).first()):
        return None

    return Comment.objects.create(user=user,
                                  expert=order.expert,
                                  rate=rate,
                                  description=description)
