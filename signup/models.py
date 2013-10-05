from django.db import models
from django.contrib.auth.models import User


class Trip(models.Model):

    name = models.CharField(max_length=100)
    blurb = models.TextField()
    cost_doc = models.PositiveIntegerField()
    cost_non_doc = models.PositiveIntegerField()
    
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    leaders = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name

class Trippee(models.Model):
    """ eventually change this to a User for authentication. """
    name = models.CharField(max_length=400)
    email = models.EmailField()
    dash = models.CharField(max_length=20)
    dietary_restrictions = models.CharField(max_length=400, blank=True)
    
    trip = models.ForeignKey(Trip)

    def __unicode__(self):
        return self.name
