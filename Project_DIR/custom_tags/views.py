from django.shortcuts import render
from .models import CustomTags
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def custom_tags(request):
    custom_tags = CustomTags.objects.all().order_by('value')

    context_dict ={'custom_tags':custom_tags}
    return render(request, 'core/feed.html', context_dict)
