from django.conf.urls import patterns, include, url
from django.contrib import admin

import cas

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^signup/', include('signup.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', cas.views.login, name='login'),
    url(r'^accounts/logout/$', cas.views.logout, name='logout'),            
)
