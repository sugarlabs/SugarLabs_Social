from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, loader
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from taggit.models import Tag
from urllib.parse import urlsplit


def post(request, tag_slug=None):
    username = request.user.username
    latest_posts = Post.objects.all().order_by('-created_at')
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        latest_posts = latest_posts.filter(tags__in=[tag])

    context_dict={'username':username,
                  'latest_posts':latest_posts,
                  'tag':tag
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
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            form.save_m2m()
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
@login_required
def edit_post(request, post_url):
    pk = request.user.pk
    user = User.objects.get(pk=pk)
    post = get_object_or_404(Post, title=post_url.replace('_', ' '))


    if request.user.is_authenticated and post.author.id == user.id:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance =post)

            if form.is_valid():
                instance = form.save(commit = False)
                instance.author = request.user
                instance.save()
                return HttpResponseRedirect('/post/{post_url}'.format(post_url=post.title.replace(' ', '_')))
            else:
                print(form.errors)
        else:
            form = PostForm()

    else:
        raise PermissionDenied

    return render(request, 'core/edit.html', {'form':form})

@login_required
def delete_post(request, post_url):
    pk = request.user.pk
    user = User.objects.get(pk=pk)
    post= get_object_or_404(Post, title = post_url.replace('_', ' '))
    if request.user.is_authenticated and post.author.id == user.id:
        if request.method=='POST':
            post.delete()
            return redirect('/accounts/{username}'.format(username = user.username))
    else:
        raise PermissionDenied
    return render(request, 'core/delete.html', {'object':post})


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
