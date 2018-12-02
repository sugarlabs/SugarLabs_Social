from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from post.models import Post
from blog.models import Blog
from .models import CustomTags
from itertools import chain



#feed view
@login_required
def feed(request, tag_slug=None):
    username = request.user.username
    latest_posts = Post.objects.all()
    latest_blogs = Blog.objects.all()
    querysets = [latest_posts, latest_blogs]
    latest_feed = list(chain(*querysets))
    latest_feed.sort(key=lambda x: x.created_at, reverse=True)
    all_custom_tags = CustomTags.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        latest_posts = latest_posts.filter(tags__in=[tag])

    #pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(latest_feed, 3)
    try:
        paginated_feed = paginator.page(page)
    except PageNotAnInteger:
        paginated_feed = paginator.page(1)
    except EmptyPage:
        paginated_feed = paginator.page(paginator.num_pages)

    context_dict={'username':username,
                  'latest_feed':paginated_feed,
                  'tag':tag,
                  'custom_tags':all_custom_tags

    }

    for feed in latest_feed:
        feed.url = feed.title.replace(' ', '_')

    return render(request, 'core/feed.html', context_dict)
