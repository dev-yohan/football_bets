from django.db import models
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify


# Create your models here.

#Model for football leagues
class League(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField(max_length=1000)
    logo = CloudinaryField('image', blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True, null=True)
       
    def __unicode__(self):
        return unicode(self.name)
    
    def save(self, *args, **kwargs):
      if not self.id:  
        self.slug = slugify(self.name)
      super(League, self).save(*args, **kwargs)
      
      
      
#Model for league seasons
class Season(models.Model):
    name = models.CharField(max_length=200) 
    initial_date = models.DateTimeField('initial date', blank=True, null=True)
    final_date = models.DateTimeField('final date', blank=True, null=True)
    league = models.ForeignKey(League)
    
    
    def __unicode__(self):
        return unicode(self.name)
    
    def save(self, *args, **kwargs):
      if not self.id:  
        self.slug = slugify(self.name)
      super(Season, self).save(*args, **kwargs)    

#Model for team's Season status
class SeasonStatus(models.Model):
    
    name = models.CharField(max_length=200)
    
    matches_played = models.DecimalField(max_digits=5, decimal_places=0)
    matches_won = models.DecimalField(max_digits=5, decimal_places=0)
    matches_draw = models.DecimalField(max_digits=5, decimal_places=0)
    matches_lost = models.DecimalField(max_digits=5, decimal_places=0)
    goals_for = models.DecimalField(max_digits=5, decimal_places=0)
    goals_against = models.DecimalField(max_digits=5, decimal_places=0)
    goals_difference = models.IntegerField()
    
    points =  models.FloatField()
    
    current_season = models.ForeignKey(Season, blank=True, null=True)  
    team = models.ForeignKey("teams.Team", blank=True, null=True) 
    
    def __unicode__(self):
        return unicode(self.name)