
from django.contrib import admin
from signup.models import Trip, Trippee

class TrippeeInline(admin.TabularInline):
    model = Trippee
    
class TripAdmin(admin.ModelAdmin):
    inlines = [TrippeeInline,]

admin.site.register(Trip, TripAdmin)
# admin.site.register(Trippee)
