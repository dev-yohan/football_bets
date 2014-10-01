from django.contrib import admin
from activities.models import Activity, ActivityByUser

admin.site.register(Activity)
admin.site.register(ActivityByUser)