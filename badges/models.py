from django.db import models
from cloudinary.models import CloudinaryField
from activities.models import Activity
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.

# Model for badges

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


# Model for badges for Activity

class BadgeByActivity(models.Model):

    activity = models.ForeignKey(Activity,
                                 related_name='related_activity',
                                 blank=True, null=True)
    badge = models.ForeignKey("badges.Badge", related_name='related_badge',
                              blank=True, null=True)
    

    def __unicode__(self):
        return unicode(self.activity.name)


#Model for user badges
class BadgeByUser(models.Model):

    user = models.ForeignKey(User)
    badge = models.ForeignKey("badges.Badge", related_name='user_badge',
                              blank=True, null=True)
    
    def __unicode__(self):
        return unicode(self.badge.name)
			
    
