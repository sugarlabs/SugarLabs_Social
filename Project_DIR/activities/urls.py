from django.conf.urls import url
from activities import views

urlpatterns = [
    url(r'^$', views.activities, name = 'activities'),
    url(r'^(?P<activity_url>\w+)/$', views.activity, name='activity'),
    
]