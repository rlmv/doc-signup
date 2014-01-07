from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


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

    trip = models.ForeignKey(Trip)    
    trippee = models.ForeignKey(User)
    dash = models.CharField(max_length=20) # can't just use netid
    dietary_restrictions = models.CharField(max_length=400, blank=True)

    def __unicode__(self):
        return "%s is registered for %s trip." % (self.trippee, self.trip)


class UserProfile(models.Model):
    """ Model to extend the User class."""
    user = models.OneToOneField(User, unique=True)
    netid = models.CharField(max_length=40)
    is_leader = models.BooleanField(default=False)

# Link UserProfile to User objects
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)
post_save.connect(create_profile, sender=User)
