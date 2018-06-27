from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.html import mark_safe

from markdown import markdown

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    tag = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))
