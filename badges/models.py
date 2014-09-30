from django.db import models
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

# Create your models here.

#Model for badges
class Badge(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField(max_length=1000)
    logo = CloudinaryField('image', blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    
    
    def __unicode__(self):
        return unicode(self.name)
    
    def save(self, *args, **kwargs):
      if not self.id:  
        self.slug = slugify(self.name)
      super(Badge, self).save(*args, **kwargs)