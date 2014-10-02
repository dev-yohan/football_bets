from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'football_bets.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^teams/', include('teams.urls', namespace="teams")),
    url(r'^badges/', include('badges.urls', namespace="badges")),
    url(r'^leagues/', include('leagues.urls', namespace="leagues")),
    url(r'^matches/', include('matches.urls', namespace="matches")),
    url(r'^$', 'matches.views.index'), 
    url(r'^admin/', include(admin.site.urls)),
)
