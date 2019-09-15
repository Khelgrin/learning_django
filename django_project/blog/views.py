from django.shortcuts import render
from .models import Post

def home(request):
    """The render function from django.shotrcuts
       is a shortcut for:
    - loading the template in,
    - render it,
    - pass that to the HTTP response"""
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
