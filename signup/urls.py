

from django.conf.urls import patterns, url

from signup import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<trip_id>\d+)/$', views.signup, name='signup'),
    url(r'^(?P<trip_id>\d+)/success/$', views.success, name='success'),
)
