from django.contrib import admin

# Register your models here.
from leagues.models import League, Season


admin.site.register(League)
admin.site.register(Season)