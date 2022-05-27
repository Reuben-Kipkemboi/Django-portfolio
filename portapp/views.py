from django.shortcuts import render
from django.http import Http404
from .models import Project
 
# Create your views here.

def portfolio_home(request):
    return render(request, 'index.html')


def project(request):
    try:
        #query all the projects
        project = Project.objects.all()
    except Project.DoesNotExist:
        raise Http404()
    print(project)
    return render(request,'projects.html', {"project":project})

def certifications(request):
    return render(request, 'certifications.html')


