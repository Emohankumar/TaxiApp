from __future__ import unicode_literals

from rest_framework.response import Response
from .models import Ride, AppUser
from rest_framework.decorators import api_view
from rest_framework import status
from math import radians, sin, cos, acos
from django.db.models import F


@api_view(['PUT'])
def setLocation(request):
    """
    Function for user to set the location.
    :param request:
    :return:
    """
    try:
        # Fetch user info from request.
        user = request.user.appuser
        # Set the user location and save.
        user.location = "{},{}".format(request.data['lat'],
                                  request.data['long'])
        user.save()
        return Response("Location updated Successfully",
                        status=status.HTTP_200_OK)
    except:
        # Return for unauthorized users.
        return Response("Not a authorized user",
                        status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
def requestRide(request):
    """
    Function for creating the ride for the user if it doesn't exists.
    :param request:
    :return:
    """
    try:
        # Fetch user info from request.
        user = request.user.appuser
        if not user.location:
            return Response("Please set your location before requesting for ride",
                            status=status.HTTP_200_OK)
        if not Ride.objects.filter(
                rider=user, is_current_ride=True).exists():
            Ride.objects.create(rider=user)
            return Response("Your request for ride made successfully.",
                            status=status.HTTP_200_OK)
        else:
            # Unable to book a ride as user current ride still in progress.
            return Response("Unable to book a ride as your current ride still in progress",
                            status=status.HTTP_200_OK)
    except:
        # Return for unauthorized users.
        return Response("Not a authorized user",
                        status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
def isRideAccepted(request):
    """
    Function for fetching the ride status for a user.
    :param request:
    :return: Sending the status for the ride
    """
    try:
        user = request.user.appuser
        # Fetching the current ride of the user.
        ride_info = Ride.objects.filter(rider=user, is_current_ride=True)
        if ride_info.exists():
            ride = ride_info.first()
            # Checking the status of the current ride.
            if ride.status == "Accepted":
                # Returning the accepted driver info.
                return Response("Your ride got accepted by driver {}".format(
                    ride.driver.user.username))
            else:
                # Returning if no driver accepted the ride.
                return Response("Your ride is not yet accepted.")
        else:
            # Returning if there is no current ride for that user.
            return Response("You have not yet requested for any ride.")
    except:
        # Return for unauthorized users.
        return Response("Not a authorized user",
                        status=status.HTTP_401_UNAUTHORIZED)


def fetch_rides_based_on_dist(rides_info, lat, lon):
    """
    Function for rides_info location from latitude and longitude
    :param rides_info:
    :param lat:
    :param lon:
    :return:
    """
    return sorted(rides_info, key=lambda x: 6371.01 * acos(
        sin(radians(float(lat)))*sin(radians(
            float(x["location"].split(",")[0]))) + cos(
            radians(float(lat)))*cos(radians(
            float(x["location"].split(",")[0])))*cos(
            radians(float(lon)) - radians(
                float(x["location"].split(",")[1])))))


@api_view(["POST"])
def getAvailableRides(request):
    """
    Function for user set location and request ride
    :param request:
    :return:
    """
    try:
        # Fetch the  driver info from request
        user = request.user.appdriver
        # Set the latitude
        lat = request.data['lat']
        # Set the longitude
        long = request.data['long']
        # Fetching the drive is avalilable
        rides = Ride.objects.filter(status="Pending").exclude(
            rider__location="").annotate(username=F(
            "rider__user__username"), location=F(
            "rider__location")).values("id", "username", "location")
        rides_info = fetch_rides_based_on_dist(rides, lat, long)
        # Returning the valid driver and set the location
        return Response(rides_info, status=status.HTTP_200_OK)
    except:
        # Returning the driver is not a valid
        return Response("Not a valid Driver")


@api_view(["PUT"])
def acceptRide(request):
    """
    Function for driver accept the ride

    :param request:
    :return:
    """
    try:
        # Fetching the driver info form request
        user = request.user.appdriver
        # Set the id for ride
        ride_id = request.data['ride_id']
        # Fetching the riding status
        ride_obj = Ride.objects.filter(id=ride_id, status="Pending")
        # Set the drive is accepted the ride
        if ride_obj.exists():
            ride = ride_obj.first()
            ride.driver = user
            ride.status = "Accepted"
            ride.is_current_ride = False
            ride.save(update_fields=["driver", "status", "is_current_ride"])
            # Returning the driver accepted the ride
            return Response("Ride Accepted Successfully", status=status.HTTP_200_OK)
        else:
            # Returning the driver no such ride
            return Response("No such Ride", status=status.HTTP_400_BAD_REQUEST)
    except:
        # Returning the driver is not valid
        return Response("Not a valid Driver")
