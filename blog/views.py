from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Author1',
        'title': 'Title1',
        'content': 'Content1',
        'date_posted': 'date..'
    },
    {
        'author': 'Author2',
        'title': 'Title2',
        'content': 'Content2',
        'date_posted': 'date2..'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
