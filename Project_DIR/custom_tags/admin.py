from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import CustomTags

class CustomTagsAdmin(admin.ModelAdmin):
    pass
admin.site.register(CustomTags, CustomTagsAdmin)
