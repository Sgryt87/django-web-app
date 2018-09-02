from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = Post.objects.all()


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
