from django.db import models
from teams.models import Team
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

    