from django.conf.urls import url
from Hello_world import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
