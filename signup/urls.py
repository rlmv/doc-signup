

from django.conf.urls import patterns, url

from signup import views

urlpatterns = patterns('',
    url(r'^$', views.test, name='test'),
)
