from django.db import models

from herfeei.common.models import BaseModel


class Comment(BaseModel):
    class CommentStatus(models.TextChoices):
        APPROVE = "APPROVE"
        REJECT = "REJECT"
        WAIT = "WAIT"

    user = models.ForeignKey("users.BaseUser", on_delete=models.CASCADE, related_name="comments")
    expert = models.ForeignKey("experts.Expert", on_delete=models.CASCADE, related_name="comments")
    rate = models.PositiveSmallIntegerField(default=3)
    description = models.CharField(max_length=512)
    status = models.CharField(max_length=7, default=CommentStatus.WAIT, choices=CommentStatus.choices)

    def __str__(self):
        return f"{self.user}"
