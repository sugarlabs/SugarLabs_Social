from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


def post(request):
    username = request.user.username
    latest_posts = Post.objects.all().order_by('-created_at')
    id = Post.objects.get(title='Test')
    context_dict={'username':username,
                  'latest_posts':latest_posts,
                  'id':id,
    }

    for post in latest_posts:
        post.url = post.title.replace(' ', '_')

    return render(request, 'core/posts.html', context_dict)


# def post_create(request):
#     return HttpResponse("<h1>create</h1>")


def post_detail(request, post_url):
    username = request.user.username
    single_post = get_object_or_404(Post, title=post_url.replace('_', ' '))
    context_dict={'username':username,
                  'single_post':single_post,
    }
    return render(request, 'core/post.html', context_dict)


@login_required
def add_post(request):
    username = request.user.username
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return redirect(post)
        else:
            print(form.errors)
    else:
        form = PostForm()

    return render(request, 'core/add_post.html', {'form':form, 'username':username,})
#
#
# def post_delete(request):
#     return HttpResponse("<h1>create</h1>")
