from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.conf import settings
from markdown import markdown

# Create your models here.
class Activities(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=500)
    about = models.TextField(max_length=200000)
    download_link = models.URLField(max_length=500)
    version = models.CharField(max_length=200)
    supported_device = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now_add=True)
    homepage = models.URLField(max_length=500)
    info = models.TextField(max_length=200000)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    Communications_and_Language = 'Communications and Language'
    Search_and_Discovery = 'Search & Discovery'
    Documents = 'Documents'
    News = 'News'
    Chat_mail_and_talk = 'Chat, mail and talk'
    Media_creation = 'Media creation'
    Programming = 'Programming'
    Maths_and_Science='Maths & Science'
    Maps_and_Geography='Maps & Geography'
    Media_players='Media players'
    Games='Games'
    Teacher_tools='Teacher tools'
    Utilities='Utilities'
    Web='Web'
    collections = 'collections'
    NA = 'NA'
    categories_choices = (
        (Communications_and_Language , 'Communications and Language'),
        (Search_and_Discovery , 'Search & Discovery'),
        (Documents , 'Documents'),
        (News , 'News'),
        (Chat_mail_and_talk , 'Chat, mail and talk'),
        (Media_creation , 'Media creation'),
        (Programming , 'Programming'),
        (Maths_and_Science,'Maths & Science'),
        (Maps_and_Geography,'Maps & Geography'),
        (Media_players,'Media players'),
        (Games,'Games'),
        (Teacher_tools,'Teacher tools'),
        (Utilities,'Utilities'),
        (Web,'Web'),
        (collections,'collections'),
        (NA ,'NA')
    )
    
    category = models.CharField(
        max_length=100,
        choices = categories_choices,
        default = NA
    )

    def __str__(self):
        return self.title

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.about, safe_mode='escape'))

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.info, safe_mode='escape'))
