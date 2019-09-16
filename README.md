# TaxiApp
Testing Tokens:
user1 : 6aed296f94b5c3c8a8a0f8f220d25b44dfe7bbdd
user2: 7a02cd4bfc0b6066795dbfd85642c69d5966f8e0
driver1: ce56e331a0a6c1202c5f0491666ebda6bf1a63ee
driver2: d029f29835f6d0c272e0c97d46ece96cc8266123


1) Get Avaiable Rides
URL: localhost:8000/api/get_available_rides/
method: POST

Headers:
Key: Authorization
Value: Token <user token>

body:
{"lat": "12.56789",
"long": "54.12345432"
}


2) Is Ride Accepted
URL: localhost:8000/api/is_ride_accepted/

method: GET

Headers:
Key: Authorization
Value: Token <user token>

3) Accept Ride

URL: localhost:8000/api/accept_ride/
method: PUT
Headers:
Key: Authorization
Value: Token <user token>

body:
{"ride_id": 1}


4) GetAvailableRides

URL: localhost:8000/api/get_available_rides/
method: POST
Headers:
Key: Authorization
Value: Token <user token>
  
5) acceptRide

URL: localhost:8000/api/accept_ride/
method: PUT
Headers:
Key: Authorization
Value: Token <user token>
