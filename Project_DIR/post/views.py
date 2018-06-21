from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post


@login_required
def post(request):
    username = request.user.username
    latest_posts = Post.objects.all().order_by('-created_at')
    context_dict={'username':username,
                  'latest_posts':latest_posts,
    }
    return render(request, 'core/posts.html', context_dict)
