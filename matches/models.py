from django.db import models
from django.template.defaultfilters import slugify
from leagues.models import League, Season
from teams.models import Team
from django.contrib.auth.models import User
from django.conf import settings


#Model for football matchs
class Match(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    match_date = models.DateTimeField('match date', blank=True, null=True)
    
    home = models.ForeignKey(Team, related_name='home')
    away = models.ForeignKey(Team, related_name='away')
    
    home_goals = models.DecimalField(max_digits=5, decimal_places=0, null=True)
    away_goals = models.DecimalField(max_digits=5, decimal_places=0, null=True)
    
    league = models.ForeignKey(League)
    season = models.ForeignKey(Season, blank=True, null=True)
    
    def __unicode__(self):
        return unicode(self.name)
    
    def save(self, *args, **kwargs):
      if not self.id:  
        self.slug = slugify(self.name)
      super(Match, self).save(*args, **kwargs)


  
      
#Model for crowd matches results
class CrowdResult(models.Model):
    user = models.ForeignKey(User)
    created_date = models.DateTimeField('match date', blank=True, null=True)
    match = models.ForeignKey(Match, related_name='match')
   
    



