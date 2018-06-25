from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.blog, name="blog"),
    url(r'^add_blog/', views.add_blog, name='add_blog'),
    url(r'^(?P<blog_url>\w+)/$', views.blog_detail, name='blog_detail'),
]
