from django import forms
from .models import Blog
from pagedown.widgets import PagedownWidget


class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=PagedownWidget)

    class Meta:
            model = Blog
            fields = ['title', 'content', 'tag', 'image']
