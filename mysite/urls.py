from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trips.views.home', name='home'),
    # url(r'^trips/', include('trips.foo.urls')),

    url(r'^signup/', include('signup.urls')),
    url(r'^admin/', include(admin.site.urls)),
                       
)
