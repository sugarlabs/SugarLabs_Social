from django.conf.urls import url, include
from blog import views

urlpatterns = [
    url(r'^$', views.blog, name="blog"),
    url(r'^add_blog/', views.add_blog, name='add_blog'),
    url(r'^(?P<blog_url>\w+)/$', views.blog_detail, name='blog_detail'),
    url(r'^(?P<blog_url>\w+)/edit/$', views.edit_blog, name='edit_blog'),
    url(r'^delete/<int:pk>', views.delete_blog, name='delete_blog')
]
