from django.contrib import admin

# Register your models here.
from matches.models import Match, CrowdResult

admin.site.register(Match)
admin.site.register(CrowdResult)