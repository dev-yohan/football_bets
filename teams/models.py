from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return unicode(self.name)

class Team(models.Model):
    name = models.CharField(max_length=200)
    logo = CloudinaryField('image', blank=True, null=True)
    league = models.ForeignKey(League)
    
    def __unicode__(self):
        return unicode(self.name)
    
    

    