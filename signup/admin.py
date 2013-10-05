
from django.contrib import admin
from django.contrib.auth.models import User

from signup.models import Trip, Trippee

class TrippeeInline(admin.TabularInline):
    model = Trippee
    extra = 0

class LeaderInline(admin.TabularInline):
    """ For nicer display of leaders in the admin. """
    model = Trip.leaders.through
    extra = 0
    
class TripAdmin(admin.ModelAdmin):
    inlines = [TrippeeInline, LeaderInline]
    exclude = ['leaders']

admin.site.register(Trip, TripAdmin)
# admin.site.register(Trippee)
