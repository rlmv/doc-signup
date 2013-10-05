

from django.http import HttpResponse

from signup.models import Trip


def index(request):

    latest_trips = Trip.objects.order_by('-start_time')[:5]
    return HttpResponse(' '.join([t.name for t in latest_trips]))
