from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name=('Profile Picture'),
                            upload_to='images', blank=True, null=True)
    bio = models.TextField(default='', blank=True)
    website = models.URLField(default='', blank=True)
    role = models.CharField(max_length=200, default='', blank=True)
    organization = models.CharField(max_length=200, default='', blank=True)
    github_handle = models.URLField(default='', blank=True, null=True)
    linkedin_handle = models.URLField(default='', blank=True, null=True)
    irc_name = models.CharField(max_length=100, default='', blank=True, null=True)
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    sex_choices = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    sex = models.CharField(max_length=100, choices= sex_choices, default='', blank=True, null=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        user_profile = UserProfile(user=user)
        user_profile.save()
post_save.connect(create_profile, sender=User)