from django.conf.urls import url
from post import views

urlpatterns = [
    url(r'^$', views.post, name='post'),
    url(r'^add_post/', views.add_post, name='add_post'),
    url(r'^(?P<post_url>\w+)/$', views.post_detail, name='post_detail'),
        url(r'^(?P<post_url>\w+)/edit/$', views.edit_post, name='edit_post'),
    url(r'^(?P<post_url>\w+)/delete/$', views.delete_post, name='delete_post')
    
]
