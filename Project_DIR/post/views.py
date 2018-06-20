from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def post(request):
    username = request.user.username
    context_dict={'username':username}
    return render(request, 'core/posts.html', context_dict)
