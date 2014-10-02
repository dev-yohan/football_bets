from django.conf.urls import patterns, url
from badges import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)