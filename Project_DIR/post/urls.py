from django.conf.urls import url
from post import views

urlpatterns = [
    url(r'^$', views.post, name='post'),
    url(r'^(?P<post_url>\w+)/$', views.post_detail, name='post_detail'),
]
