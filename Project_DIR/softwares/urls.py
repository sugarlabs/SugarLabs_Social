from django.conf.urls import url
from softwares import views

urlpatterns = [
    url(r'^$', views.softwares, name = 'softwares'),
    url(r'^(?P<software_url>\w+)/$', views.software, name='software'),
    
]
