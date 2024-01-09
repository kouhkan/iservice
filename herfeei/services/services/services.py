from typing import List

from django.db.models import QuerySet

from herfeei.services.models import UserAnswer, QuestionItem
from herfeei.users.models import BaseUser


def create_user_answers(*, user: BaseUser, answers: List[QuestionItem]) -> QuerySet[UserAnswer]:
    instance = UserAnswer.objects.create(user=user)
    instance.answers.set(answers)
    return instance
