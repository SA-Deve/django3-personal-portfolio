from django.shortcuts import render
from .models import Blog

def home(request):
    blogs = Blog.objects.order_by('-date')
    context = {'blogs':blogs}
    return render(request, 'html/blog/home.html', context)

def detail(request,blog_id):
    item = Blog.objects.get(id=blog_id)
    context = {'item': item}
    return render(request, 'html/blog/detail.html', context)

