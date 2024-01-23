from django.urls import path

from herfeei.comments.apis.comments import CreateCommentView

urlpatterns = [
    path("", CreateCommentView.as_view(), name="create-comment"),
]
