from django.db import models
from django.utils.html import mark_safe
from markdown import markdown

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    RUNNING = 'RN'
    UPCOMING = 'UPCMG'
    COMPLETED = 'CMPLTD'
    status_choices = (
        (RUNNING, 'Running'),
        (UPCOMING, 'Upcoming'),
        (COMPLETED, 'Completed')
    )
    status = models.CharField(
        max_length = 2,
        choices = status_choices
    )
    WEB = 'WB'
    SOFTWARE = 'SWRE'
    HARDWARE = 'HWRE'
    NA = 'NA'
    category_choices = (
        (WEB, 'Web'),
        (SOFTWARE, 'software'),
        (HARDWARE, 'Hardware'),
        (NA, 'NA')
    )
    category = models.CharField(
        max_length = 2,
        choices=category_choices,
        default=NA
    )
    project_website = models.URLField(max_length = 200)
    irc_channel = models.URLField(max_length = 200)
    mailing_list = models.URLField(max_length = 200)
    info = models.TextField(max_length=200000)
    setup_guide = models.TextField(max_length=200000)
    contribution_guide = models.TextField(max_length=200000)

    def __str__(self):
        return self.title

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.info, safe_mode='escape'))

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.setup_guide, safe_mode='escape'))

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.contribution_guide, safe_mode='escape'))
