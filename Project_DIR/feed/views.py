from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from post.models import Post


#feed view
@login_required
def feed(request):
    username = request.user.username
    latest_feed = Post.objects.all().order_by('-created_at')
    context_dict={'username':username,
                  'latest_feed':latest_feed,
    }

    for feed in latest_feed:
        feed.url = feed.title.replace(' ', '_')

    return render(request, 'core/feed.html', context_dict)
