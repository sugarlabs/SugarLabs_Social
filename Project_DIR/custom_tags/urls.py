from django.conf.urls import url
from custom_tags import views

urlpatterns = [
    url(r'^$', views.custom_tags, name='custom_tags'),
]
