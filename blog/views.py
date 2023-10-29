from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Yakubov",
        "date": date(2021, 7, 21),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Hiking, a form of exercise older than exercise itself, is so hot right now. 
          From 2018 to 2021, the number of Americans hitting the trails ballooned from 
          around 48 million to 59 million, according to the nonprofit Outdoor Foundation.
          Though they came because of the pandemic, many people have stayed for the 
          workout and for the refuge hiking offers from their screen-addled daily lives. 
          For Alyson Chun, an outdoors guide and assistant director of adventure sports at Stanford, 
          hiking offers freedom and perspective. She said it helps her reconnect with 
          “the grandness of the world” whenever she feels bogged down by daily life.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Yakubov",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
        Visual Studio Code is one of the most popular and powerful text editors used by software engineers today.
        In this article, we will go over the steps necessary to download a popular text editor called Visual 
        Studio Code, also referred to as “VS Code.” By the end of the article you will be able to create 
        a folder in Visual Studio Code that contains an HTML document that you can open in your web browser.

        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Yakubov",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Forests are the lungs of the world, helping to keep our 
          climate stable and providing 40% of the planet’s oxygen. 
          They regulate our water system, increase rainfall and improve the quality of the water we need to survive. 
          Over 1.6 billion peoples’ livelihoods depend on forests, and forests are home to many Indigenous peoples 
          and communities who steward some of the earth’s most fragile ecosystems.
        """
    }
]


# Create your views here.

def get_date(post):
    return post['date']


def start_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html",
                  {"posts": latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {"all_posts": all_posts})


def post_details(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})
