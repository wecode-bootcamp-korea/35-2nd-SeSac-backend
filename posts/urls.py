from django.urls import path

from .views import PostListView, PostView

urlpatterns = [
    path('', PostListView.as_view()),
    path('/posting', PostView.as_view()),
]