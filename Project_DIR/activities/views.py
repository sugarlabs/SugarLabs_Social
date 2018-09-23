from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, loader
from django.urls import reverse
from .models import Activities
from urllib.parse import urlsplit


def activities(request):
    all_activities = Activities.objects.all()
    categories = Activities._meta.get_field('category').choices
    context_dict = {
                    'activities':all_activities,
                    'categories':categories
    }

    for activities in all_activities:
        activities.url = activities.title.replace(' ', '_')

    return render(request, 'core/activities.html', context_dict)

def activity(request, activity_url):
    activity = get_object_or_404(Activities, title=activity_url.replace('_', ' '))
    context_dict = {
                'activity':activity
    }

    return render(request, 'core/activity.html', context_dict)


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

