
from django.contrib import admin
from django.contrib.auth.models import User

from signup.models import Trip, Signup

class SignupInline(admin.TabularInline):
    model = Signup
    extra = 0

class LeaderInline(admin.TabularInline):
    """ Display the leaders with a nicer interface.

    TODO: Fix labels to say 'Leaders', not Trip-User
    relationship, or whatever it is now.
    """
    
    model = Trip.leaders.through
    extra = 0
    
class TripAdmin(admin.ModelAdmin):
    """ Admin view for Trips."""
    inlines = [SignupInline, LeaderInline]
    exclude = ['leaders']      # dispayed in LeaderInline

admin.site.register(Trip, TripAdmin)

