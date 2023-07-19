from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="landing-page"),
    path("posts", views.all_posts, name="all-posts-page"),
    path(
        "posts/<slug:slug>", views.indv_post, name="indv-post-page"
    ),  # i.e. /posts/first-post
]
