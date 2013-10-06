from django.db import models
from django.contrib.auth.models import User

class Trip(models.Model):
    """ Represents a trip in the database.

    Other potential fields:
      * max # of trippees <-- this is an important one,
        but we need to implement a mechanism for rejecting
        people / creating a waitlist.
      * difficulty / length
      * links (to maps, pictures, etc.)
    """
    
    name = models.CharField(max_length=100)
    blurb = models.TextField()
    cost_doc = models.PositiveIntegerField()
    cost_non_doc = models.PositiveIntegerField()
    
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    leaders = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name

class Signup(models.Model):
    """ Represents one trippee's registration for a trip.
    
    TODO: eventually link this to a User for authentication,
    i.e., add a ForeignKey(User) field.
    """
    
    name = models.CharField(max_length=400)
    email = models.EmailField()
    dash = models.CharField(max_length=20)
    dietary_restrictions = models.CharField(max_length=400, blank=True)
    
    trip = models.ForeignKey(Trip)

    def __unicode__(self):
        return self.name
