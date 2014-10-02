from django.contrib import admin
from activities.models import Activity, ActivityByUser

#models to be visible on CMS
admin.site.register(Activity)
admin.site.register(ActivityByUser)