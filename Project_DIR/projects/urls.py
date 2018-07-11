from django.conf.urls import url
from projects import views

urlpatterns = [
    url(r'^$', views.projects, name = 'projects'),
    url(r'^(?P<project_url>\w+)/$', views.project, name='project'),
]
