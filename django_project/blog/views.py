from django.shortcuts import render


posts = [
    {
        'author': 'Khel',
        'title': 'title1',
        'content': 'first post',
        'date': '21.10.2018'
    },
    {
        'author': 'Khel2',
        'title': 'title2',
        'content': 'second post',
        'date': '21.10.2019'
    }
]


def home(request):
    """The render function from django.shotrcuts
       is a shortcut for:
    - loading the template in,
    - render it,
    - pass that to the HTTP response"""
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
