from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, loader
from django.urls import reverse
from .models import Software
from urllib.parse import urlsplit

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

def software(request, software_url):
    username = request.user.username
    software = get_object_or_404(Software, title=software_url.replace('_', ' '))
    context_dict = {'username':username,
                'software':software
    }

    return render(request, 'core/software.html', context_dict)

#comment redirect after posting
def comment_posted( request ):
    referer = request.META.get('HTTP_REFERER', None)
    if referer is None:
        pass
    try:
        redirect_to = urlsplit(referer, 'http', False)[2]
    except IndexError:
       pass
    return HttpResponseRedirect(redirect_to)

