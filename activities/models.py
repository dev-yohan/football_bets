from django.db import models
from django.template.defaultfilters import slugify
from badges.models import Badge
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

#Model for activities
class Activity(models.Model):
    name = models.CharField(max_length=255)
    keyword = models.CharField(max_length=255)
    short_description = models.TextField(max_length=1000)
    
    def __unicode__(self):
        return unicode(self.name)
    
    def save(self, *args, **kwargs):
      if not self.id:  
        self.slug = slugify(self.name)
      super(Activity, self).save(*args, **kwargs)


#Model for user's activities
class ActivityByUser(models.Model):
    user = models.ForeignKey(User)
    activity = models.ForeignKey(Activity, blank=True, null=True)
    badge = models.ForeignKey(Badge, blank=True, null=True)
    created_date = models.DateTimeField('activity date', blank=True, null=True)
    first_time = models.BooleanField()
    
    def __unicode__(self):
        return unicode(self.activity.name)
    


