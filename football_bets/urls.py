from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'football_bets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^teams/', include('teams.urls', namespace="teams")),
    url(r'^admin/', include(admin.site.urls)),
)
