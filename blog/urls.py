from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_page, name="start_page"),
    path("posts", views.posts, name="posts_page"),
    path("posts/<slug:slug>", views.post_details, name="post_details_page"),
]
