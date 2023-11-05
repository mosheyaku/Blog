from django.shortcuts import render
from datetime import date
from .models import Post

all_posts = [

]


# Create your views here.

def get_date(post):
    return post['date']


def start_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, "blog/index.html",
                  {"posts": latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_details(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
