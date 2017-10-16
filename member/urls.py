from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^dashboard/(?P<member_code>[0-9a-zA-Z]+)/$', views.dashboard, name='dashboard'),
    url(r'^profile/(?P<member_code>[0-9a-zA-Z]+)/$', views.profile, name='profile'),
    url(r'^plants/(?P<member_code>[0-9a-zA-Z]+)/$', views.plants, name='plants'),
]