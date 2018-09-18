from django.contrib import admin
from .models import Activities


# Register your models here
class ActivitiesAdmin(admin.ModelAdmin):
    pass
admin.site.register(Activities, ActivitiesAdmin)
