
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.forms import ModelForm
from django.views import generic

from signup.models import Trip, Trippee


def SignupForm(ModelForm):
    """ Use to signup for a trip. """
    class Meta:
        model = Trippee
        fields = ['name', 'email', 'dash', 'dietary_restrictions']


class IndexView(generic.ListView):
    """ Index of existing trips. """
    
    template_name = 'signup/index.html'
    context_object_name = 'trip_list'
    
    def get_queryset(self):
        return Trip.objects.all().order_by('-start_time')
    
    
def trip_detail(request, trip_id):

    trip = get_object_or_404(Trip, pk=trip_id)
    return HttpResponse("name: %s" % trip.name)


def signup(request, trip_id):

    trip = get_object_or_404(Trip, pk=trip_id)
    
