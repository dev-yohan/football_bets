from django.db import models
from django.template.defaultfilters import slugify
from badges.models import Badge
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

#Model for activities
class Activity(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField(max_length=1000)
    badge = models.ForeignKey(Badge, blank=True, null=True)
    
    def __unicode__(self):
        return unicode(self.name)
    
    def save(self, *args, **kwargs):
      if not self.id:  
        self.slug = slugify(self.name)
      super(Activity, self).save(*args, **kwargs)