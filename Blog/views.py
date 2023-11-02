from django.shortcuts import render
from .models import Blog
from django.views import generic
# Create your views here.
def HomePage(request):
  blogs = Blog.objects.all().order_by('blog_title')
  context={
    'blogs':blogs
  }
  return render(request, 'index.html',context)

def blog_details(request,pk=None):
  blog= Blog.objects.get(id=pk)
  blogs= Blog.objects.all()
  context={
    'blog': blog,
    'blogs':blogs
  }
  return render(request, 'blog_detail.html', context)

def Register(request):
  return render(request, 'register.html')


def Login(request):
  return render(request, 'login.html')