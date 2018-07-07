from django.db import models

# Create your models here.
class CustomTags(models.Model):
    tag = models.CharField(max_length=100)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.tag
