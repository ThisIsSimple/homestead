from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^input/$', views.input, name='input'),
]