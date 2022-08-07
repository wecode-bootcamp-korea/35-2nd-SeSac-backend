from django.urls import path

from .views import PostView

urlpatterns = [
    path('/posting', PostView.as_view()),
    path('/<int:post_id>', PostView.as_view()),
    path('/edit/<int:post_id>', PostView.as_view())
]