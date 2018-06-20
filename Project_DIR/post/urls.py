from django.conf.urls import url
from post import views

urlpatterns = [
    url(r'^$', views.post, name='post'),
]
