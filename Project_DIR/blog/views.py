from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, loader
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied


def blog(request):
    username = request.user.username
    latest_blogs = Blog.objects.all().order_by('-created_at')
    context_dict={'username':username,
                  'latest_blogs':latest_blogs,
    }

    for blog in latest_blogs:
        blog.url = blog.title.replace(' ', '_')

    return render(request, 'core/blogs.html', context_dict)


# def post_create(request):
#     return HttpResponse("<h1>create</h1>")


def blog_detail(request, blog_url):
    username = request.user.username
    single_blog = get_object_or_404(Blog, title=blog_url.replace('_', ' '))
    context_dict={'username':username,
                  'single_blog':single_blog,
    }
    return render(request, 'core/blog.html', context_dict)


@login_required
def add_blog(request):
    username = request.user.username
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect(blog)
        else:
            print(form.errors)
    else:
        form = BlogForm()

    return render(request, 'core/add_blog.html', {'form':form, 'username':username,})
#
#
# def post_delete(request):
#     return HttpResponse("<h1>create</h1>")

@login_required
def edit_blog(request, blog_url):
    pk = request.user.pk
    user = User.objects.get(pk=pk)
    blog = get_object_or_404(Blog, title=blog_url.replace('_', ' '))


    if request.user.is_authenticated and blog.author == request.user.username:
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES, instance =blog)

            if form.is_valid():
                instance = form.save(commit = False)
                instance.author = request.user
                instance.save()
                return HttpResponseRedirect('/blog/{blog_url}'.format(blog_url=blog.title.replace(' ', '_')))
            else:
                print(form.errors)
        else:
            form = BlogForm()

    else:
        raise PermissionDenied

    return render(request, 'core/edit_profile.html', {'form':form})

@login_required
def delete_blog(request, blog_url):
    pk = request.user.pk
    user = User.objects.get(pk=pk)
    blog= get_object_or_404(Blog, pk=pk)    
    if request.method=='POST':
        blog.delete()
        return redirect(blog)
    return render(request, 'core/userprofile.html', {'object':blog})

