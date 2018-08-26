from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, loader
from django.urls import reverse

# Create your views here.
def softwares(request):
    username = request.user.username
    context_dict = {'username':username,
    }


    return render(request, 'core/softwares.html', context_dict)

