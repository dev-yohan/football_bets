from django.contrib import admin

# Register your models here.
from teams.models import Team, TeamPhoto


admin.site.register(Team)
admin.site.register(TeamPhoto)