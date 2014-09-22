from django.contrib import admin

# Register your models here.
from matches.models import Match, CrowdResult, ResultForecast

admin.site.register(Match)
admin.site.register(CrowdResult)
admin.site.register(ResultForecast)