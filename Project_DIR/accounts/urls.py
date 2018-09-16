from django.conf.urls import url
from accounts import views

urlpatterns = [
    url(r'^update/$', views.edit_user, name='account_update'),
    url(r'^(?P<username>\w+)/$', views.profile, name='profile'),
]