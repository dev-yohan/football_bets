from django.conf.urls import patterns, url

from teams import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<team_id>\d+)/$', views.detail, name='detail')
)