from django.contrib import admin

# Register your models here.
from teams.models import Team
from teams.models import League

admin.site.register(Team)
admin.site.register(League)