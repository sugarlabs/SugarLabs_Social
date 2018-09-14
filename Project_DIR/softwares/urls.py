from django.conf.urls import url
from softwares import views

urlpatterns = [
    url(r'^$', views.softwares, name = 'softwares'),
    
]
