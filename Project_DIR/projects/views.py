from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, loader
from django.urls import reverse
from .models import Project

# Create your views here.
def projects(request):
    username = request.user.username
    all_projects = Projects.objects.all()
    context_dict = {'username':username,
                    'projects':all_projects
    }

    for project in projects:
        project.url =  project.title.replace(' ', '_')

    return render(request, 'core/projects.html', context_dict)


def project(request, project_url):
    username = request.user.username
    project = get_object_or_404(Projects, title=project_url.replace('_', ' '))
    context_dict = {'username':username,
                'project':project
    }

    return render(request, 'core/project.html', context_dict)
