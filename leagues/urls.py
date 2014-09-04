from django.conf.urls import patterns, url

from leagues import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<league_id>[a-z\d]+)(?:/(?P<league_slug>[\w\d-]+))?/$', views.detail, name='detail')
  
)