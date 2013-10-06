from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.forms import ModelForm
from django.views import generic
from django.core.urlresolvers import reverse

from signup.models import Trip, Signup


class SignupForm(ModelForm):
    """ Use to signup for a trip. """
    class Meta:
	model = Signup
	fields = ['name', 'email', 'dash', 'dietary_restrictions']

class IndexView(generic.ListView):
    """
    Index of existing trips.
    This should be filtered to only show upcoming trips.
    """

    template_name = 'signup/index.html'
    context_object_name = 'trip_list'

    def get_queryset(self):
	return Trip.objects.all().order_by('-start_time')


def trip_detail(request, trip_id):

    trip = get_object_or_404(Trip, pk=trip_id)
    return HttpResponse("name: %s" % trip.name)


def signup(request, trip_id):
    """ Page for user signup. """
    trip = get_object_or_404(Trip, pk=trip_id)

    if request.method == 'POST':
	form = SignupForm(request.POST)

	if form.is_valid():
	    t = form.save(commit=False)
	    t.trip = trip
	    t.save()
	    url = reverse('success', kwargs={'trip_id': trip_id})
	    return HttpResponseRedirect(url)

    else:
	form = SignupForm()

    context = {
	'trip': trip,
	'signup_form': form,
    }
    return render(request, 'signup/signup.html', context)


def success(request, trip_id):
    """ Landing page after successful signup. """

    trip = get_object_or_404(Trip, pk=trip_id)
    context = {
	'trip': trip,
    }
    return render(request, 'signup/success.html', context)
