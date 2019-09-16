from django.conf.urls import url

from . import views


app_name = "taxi"
urlpatterns = [
    url(r'^set_location/$', views.setLocation, name='set_location'),
    url(r'^request_ride/$', views.requestRide, name='request_ride'),
    url(r'^is_ride_accepted/$', views.isRideAccepted, name='is_ride_accepted'),
    url(r'^get_available_rides/$', views.getAvailableRides, name='get_available_rides'),
    url(r'^accept_ride/$', views.acceptRide, name='accept_ride'),

]