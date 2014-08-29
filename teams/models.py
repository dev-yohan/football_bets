from django.db import models

# Create your models here.

class League(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):
        return unicode(self.name)

class Team(models.Model):
    name = models.CharField(max_length=200)
    league = models.ForeignKey(League)
    
    def __unicode__(self):
        return unicode(self.name)
    
    

    