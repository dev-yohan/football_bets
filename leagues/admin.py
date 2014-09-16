from django.contrib import admin
from django.contrib.admin import site, ModelAdmin

# Register your models here.
from leagues.models import League, Season, SeasonStatus
from teams.models import Team

 
admin.site.register(League)
admin.site.register(Season)
admin.site.register(SeasonStatus)