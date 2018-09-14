from django.db import models
from django.utils.html import mark_safe
from markdown import markdown

# Create your models here.
class Software(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    WEB = 'WEB'
    SUGAR = 'SUGAR'
    UBUNTU = 'UBUNTU'
    FEDORA = 'FEDORA'
    WINDOWS = 'WINDOWS'
    CHROME = 'CHROME'
    ANDROID = 'ANDROID'
    NA = 'NA'
    categories_choices = (
        (WEB , 'web'),
        (SUGAR , 'sugar'),
        (UBUNTU , 'ubuntu'),
        (FEDORA , 'fedora'),
        (WINDOWS , 'windows'),
        (CHROME , 'chrome'),
        (ANDROID , 'android'),
        (NA, 'NA')
    )
    
    category = models.CharField(
        max_length=10,
        choices = categories_choices,
        default = NA
    )

    software_source = models.URLField(max_length = 200)
    info = models.TextField(max_length=200000)
    installation_guide = models.TextField(max_length=200000)
    contribution_guide = models.TextField(max_length=200000)


    def __str__(self):
        return self.title

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.info, safe_mode='escape'))

    def get_content_as_markdown(self):
        return mark_safe(markdown(self.installation_guide, safe_mode='escape'))
        
    def get_content_as_markdown(self):
        return mark_safe(markdown(self.contribution_guide, safe_mode='escape'))
        

