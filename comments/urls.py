from django.urls import path

from comments.views import CommentView

urlpatterns = [
    path('/<int:post_id>/comments', CommentView.as_view()),
    path('/<int:post_id>/comments/<int:comment_id>', CommentView.as_view()),
]