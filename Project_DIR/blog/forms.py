from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 2, 'placeholder': 'Write your blog here?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
            model = Blog
            fields = ['title', 'content', 'tag', 'image']
