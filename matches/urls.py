from django.conf.urls import patterns, url

from matches import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<match_id>[a-z\d]+)(?:/(?P<match_slug>[\w\d-]+))?/$', views.detail, name='detail'),
    url(r'^crowd-result-list/(?P<match_id>[a-z\d]+)?/$', views.crowd_result_list, name='crowd_result_list'),
    url(r'^crowd-result/(?P<match_id>[a-z\d]+)?/$', views.create_crowd_result, name='create_crowd_result'),
)