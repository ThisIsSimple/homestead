from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.board_list, name='board_list'),
    url(r'^(?P<board_name>[0-9A-Za-z]+)/$', views.post_list, name='post_list'),
    url(r'^(?P<board_name>[0-9A-Za-z]+)/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<board_name>[0-9A-Za-z]+)/create/$', views.post_create, name='post_list'),
]
