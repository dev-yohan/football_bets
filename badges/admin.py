from django.contrib import admin
from badges.models import Badge, BadgeByActivity, BadgeByUser

admin.site.register(Badge)
admin.site.register(BadgeByActivity)
admin.site.register(BadgeByUser)
