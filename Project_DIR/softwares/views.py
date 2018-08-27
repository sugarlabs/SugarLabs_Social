from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, loader
from django.urls import reverse
from .models import Software

# Create your views here.
def softwares(request):
    username = request.user.username
    all_softwares = Software.objects.all()
    context_dict = {'username':username,
                    'softwares':all_softwares
    }

    for software in all_softwares:
        software.url = software.title.replace(' ', '_')

    return render(request, 'core/softwares.html', context_dict)

