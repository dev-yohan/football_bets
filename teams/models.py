from django.db import models
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
from leagues.models import League
from leagues.models import Season
# Create your models here.


#Model for football teams
class Team(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField(max_length=1000)
    team_photo = CloudinaryField('image', blank=True, null=True)
    logo = CloudinaryField('image', blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    
    league = models.ForeignKey(League, blank=True, null=True)
    current_season = models.ForeignKey(Season, blank=True, null=True)
    
    #league = models.ForeignKey(League)
    
    
    def __unicode__(self):
        return unicode(self.name)
    
    def save(self, *args, **kwargs):
      if not self.id:  
        self.slug = slugify(self.name)
      super(Team, self).save(*args, **kwargs)
    

#Model for team photos
class TeamPhoto(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField(max_length=1000)
    photo = CloudinaryField('image', blank=True, null=True)

    team = models.ForeignKey(Team, blank=True, null=True)
    
    def __unicode__(self):
        return unicode(self.name)
    
    def save(self, *args, **kwargs):
      if not self.id:  
        self.slug = slugify(self.name)
      super(TeamPhoto, self).save(*args, **kwargs)   

    