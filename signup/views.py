
import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.forms import ModelForm
from django.views import generic
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from signup.models import Trip, Signup

logger = logging.getLogger(__name__)


class SignupForm(ModelForm):
    """ Use to signup for a trip. """
    class Meta:
        model = Signup
	fields = [ 'dash', 'dietary_restrictions']


class IndexView(generic.ListView):
    """
    Index of existing trips.
    This should be filtered to only show upcoming trips.
    """

    template_name = 'signup/index.html'
    context_object_name = 'trip_list'

    def get_queryset(self):
	return Trip.objects.all().order_by('-start_time')

# expose view
#index = login_required(IndexView.as_view())
index = IndexView.as_view()


@login_required
def signup(request, trip_id):
    """ Page for user signup. """
    trip = get_object_or_404(Trip, pk=trip_id)

    if request.method == 'POST':
	form = SignupForm(request.POST)
        
	if form.is_valid():
	    s = form.save(commit=False)
	    s.trip = trip
            s.trippee = request.user 
	    s.save()
            logger.info('%s signed up for trip %s' %
                        (request.user.username, trip.name))
	    url = reverse('success', kwargs={'trip_id': trip_id})
	    return HttpResponseRedirect(url)

    else:
	form = SignupForm()

    context = {
	'trip': trip,
	'signup_form': form,
    }
    return render(request, 'signup/signup.html', context)


@login_required
def success(request, trip_id):
    """ Landing page after successful signup. """

    trip = get_object_or_404(Trip, pk=trip_id)
    context = {
	'trip': trip,
    }
    return render(request, 'signup/success.html', context)
