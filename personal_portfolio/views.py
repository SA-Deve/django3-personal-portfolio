from django.shortcuts import render
from .models import Project,About

def home(request):
    about = About.objects.all()
    context = {'about': about}
    return render(request, 'html/portfolio/home.html', context)

def project(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request,'html/portfolio/projects.html',context)
    
def detail(request,project_id):
    item = Project.objects.get(id=project_id)
    context = {'item':item}
    return render(request,'html/portfolio/detail.html',context)
