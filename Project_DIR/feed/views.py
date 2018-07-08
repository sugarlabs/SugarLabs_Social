from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from post.models import Post
from .models import CustomTags



#feed view
@login_required
def feed(request, tag_slug=None):
    username = request.user.username
    latest_feed = Post.objects.all().order_by('-created_at')
    all_custom_tags = CustomTags.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        latest_posts = latest_posts.filter(tags__in=[tag])

    context_dict={'username':username,
                  'latest_feed':latest_feed,
                  'tag':tag,
                  'custom_tags':all_custom_tags

    }

    for feed in latest_feed:
        feed.url = feed.title.replace(' ', '_')

    return render(request, 'core/feed.html', context_dict)
