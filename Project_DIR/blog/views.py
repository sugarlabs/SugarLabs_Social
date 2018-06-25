from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm


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
