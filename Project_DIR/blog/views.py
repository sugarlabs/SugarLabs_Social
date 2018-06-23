from django.shortcuts import render

def blog(request):
    return render(request, 'core/blog.html', {})
