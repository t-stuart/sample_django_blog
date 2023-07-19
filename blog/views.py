from datetime import date
from django.shortcuts import render

# Create your views here.
posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Norm L. Hughman",
        "date": date(2023, 7, 17),
        "title": "Mountain Hiking",
        "excerpt": "Something something nature. You won't believe what happened next. I hiked into the mountains.",
        "content": """
                        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                    Exercitationem ut magnam tempora facilis. Qui, corporis modi deleniti illo dolorum voluptas nam. 
                    Libero iusto dolor porro, numquam explicabo vero rerum voluptatibus.

                        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                    Exercitationem ut magnam tempora facilis. Qui, corporis modi deleniti illo dolorum voluptas nam. 
                    Libero iusto dolor porro, numquam explicabo vero rerum voluptatibus.

                        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                    Exercitationem ut magnam tempora facilis. Qui, corporis modi deleniti illo dolorum voluptas nam. 
                    Libero iusto dolor porro, numquam explicabo vero rerum voluptatibus.
                    """,
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Norm L. Hughman",
        "date": date(2023, 6, 17),
        "title": "Programming is Fun",
        "excerpt": "Something something Coding. You won't believe what happened next. I coded a lot",
        "content": """
                        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                    Exercitationem ut magnam tempora facilis. Qui, corporis modi deleniti illo dolorum voluptas nam. 
                    Libero iusto dolor porro, numquam explicabo vero rerum voluptatibus.

                        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                    Exercitationem ut magnam tempora facilis. Qui, corporis modi deleniti illo dolorum voluptas nam. 
                    Libero iusto dolor porro, numquam explicabo vero rerum voluptatibus.

                        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                    Exercitationem ut magnam tempora facilis. Qui, corporis modi deleniti illo dolorum voluptas nam. 
                    Libero iusto dolor porro, numquam explicabo vero rerum voluptatibus.
                    """,
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Norm L. Hughman",
        "date": date(2023, 5, 17),
        "title": "Into the Woods",
        "excerpt": "Something something nature. You won't believe what happened next. I was out in the woods",
        "content": """
                        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                    Exercitationem ut magnam tempora facilis. Qui, corporis modi deleniti illo dolorum voluptas nam. 
                    Libero iusto dolor porro, numquam explicabo vero rerum voluptatibus.

                        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                    Exercitationem ut magnam tempora facilis. Qui, corporis modi deleniti illo dolorum voluptas nam. 
                    Libero iusto dolor porro, numquam explicabo vero rerum voluptatibus.

                        Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
                    Exercitationem ut magnam tempora facilis. Qui, corporis modi deleniti illo dolorum voluptas nam. 
                    Libero iusto dolor porro, numquam explicabo vero rerum voluptatibus.
                    """,
    },
]


def get_date(post):
    return post["date"]


def landing_page(req):
    sorted_posts = sorted(posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(
        req,
        "blog/index.html",
        {
            "posts": latest_posts,
        },
    )


def all_posts(req):
    return render(req, "blog/all-posts.html")


def indv_post(req, slug):
    return render(req, "blog/post-detail.html")
