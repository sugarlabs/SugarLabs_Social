from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required


#feed view to check the login functionality
@login_required
def feed(request):
    username = request.user.username
    context_dict={'username':username}
    return render(request, 'core/feed.html', context_dict)
