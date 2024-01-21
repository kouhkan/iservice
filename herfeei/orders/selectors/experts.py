from typing import List

from django.db.models import QuerySet, Avg, Count

from herfeei.comments.models import Comment
from herfeei.experts.models import Bookmark, Expert
from herfeei.users.models import BaseUser


def get_bookmarked_experts(*, user: BaseUser) -> List[QuerySet[Bookmark]]:
    return Bookmark.objects.filter(user=user)


def get_most_rated_experts(*, service_category_slug: str) -> List[QuerySet[Expert]]:
    return (
        Expert.objects
        .filter(
            comments__status=Comment.CommentStatus.APPROVE,
            category__slug=service_category_slug
        )
        .values('category__title')
        .annotate(avg_rating=Avg('comments__rate'), num_ratings=Count('comments'))
        .order_by('-avg_rating', '-num_ratings')
    )
