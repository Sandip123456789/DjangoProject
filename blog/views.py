from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse('<h1>Blog home</h1>')

# def about(request):
#     return HttpResponse('<h1>Blog about</h1>')

#Dummy data
# posts = [
#     {
#         'author': 'sandyC',
#         'title': 'Blog post 1',
#         'content': 'First post content',
#         'date_posted': 'may 29, 2020'
#     },
#     {
#         'author': 'john doe',
#         'title': 'Blog post 2',
#         'content': 'Second post content',
#         'date_posted': 'may 30, 2020'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About' })
