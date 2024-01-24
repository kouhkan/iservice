from typing import List

from django.db.models import Avg, Count, Q, QuerySet

from herfeei.comments.models import Comment
from herfeei.experts.models import Expert, Sample
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
            Q(available__start_time__lte=start_time,
              available__end_time__gte=end_time) & Q(available__date=date))

    # Remove experts that they are busy
    suggested_experts = suggested_experts.exclude(
        orders__order_date_time__in=order.order_date_time.all())

    return suggested_experts


def get_expert(*, expert_code: str) -> Expert:
    return Expert.objects.filter(expert_code=expert_code).first()


def get_expert_rate(*, expert_code: str) -> float:
    expert_rate = Expert.objects.filter(expert_code=expert_code).annotate(
        avg_rate=Avg('comments__rate',
                     filter=Q(comments__status=Comment.CommentStatus.APPROVE)),
        comment_count=Count(
            'comments',
            filter=Q(comments__status=Comment.CommentStatus.APPROVE))).first()

    if expert_rate:
        return expert_rate.avg_rate or 0.0

    return 0.0


def get_expert_comments_count(*, expert_code: str) -> int:
    return Comment.objects.filter(
        expert__expert_code=expert_code,
        status=Comment.CommentStatus.APPROVE).count()


def get_expert_comments(*, expert_code: str) -> int:
    return Comment.objects.filter(expert__expert_code=expert_code,
                                  status=Comment.CommentStatus.APPROVE)


def get_expert_complete_orders(*, expert_code: str) -> int:
    return Order.objects.filter(expert__expert_code=expert_code,
                                is_complete=True).count()


def get_expert_samples(*, expert_code: str) -> List[QuerySet[Sample]]:
    return Sample.objects.filter(expert__expert_code=expert_code)
