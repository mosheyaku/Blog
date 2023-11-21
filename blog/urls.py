from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="start_page"),
    path("posts", views.AllPostsView.as_view(), name="posts_page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post_details_page"),
]
