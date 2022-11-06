import requests
from math import sqrt, radians, cos, sin, atan2
from .parameters import *


def get_delivery_fee(pickup_address, drop_off_address):

    url = "https://daas-public-api.development.dev.woltapi.com/merchants/"+MERCHANT_ID+"/delivery-fee"
    headers = {"Authorization": "Bearer " + API_TOKEN_KEY}

    request_body = {
      "pickup": {
        "location": {
            "formatted_address": pickup_address
        }
      },
      "dropoff": {
        "location": {
            "formatted_address": drop_off_address
        }
      }
    }

    response = requests.post(url, json=request_body, headers=headers)
    return response

def send_delivery_request(pickup_address , drop_off_address, drop_off_time):

    url = "https://daas-public-api.development.dev.woltapi.com/merchants/"+MERCHANT_ID+"/delivery-order"
    headers = {"Authorization": "Bearer " + API_TOKEN_KEY}

    request_body = {
        "pickup": {
            "location": {
                "formatted_address": pickup_address
            },
            "comment": "The box is in front of the door",
            "contact_details": {
                "name": "John Doe",
                "phone_number": "+358123456789",
                "send_tracking_link_sms": False
            }
        },
        "dropoff": {
            "location": {
                "formatted_address": drop_off_address
            },
            "contact_details": {
                "name": "Oussama Bekkouche",
                "phone_number": "+358123456789",
                "send_tracking_link_sms": False
            },
        },
        "customer_support": {
            "email": "string",
            "phone_number": "string",
            "url": "string"
        },
        "is_no_contact": False,
        "contents": [
            {
                "count": 1,
                "description": "plastic bag",
                "identifier": "12345",
                "tags": []
            }
        ],
        "tips": [],
        "min_preparation_time_minutes": 10,
        "scheduled_dropoff_time": drop_off_time

    }

    response = requests.post(url, json=request_body, headers=headers)
    return response


def compute_distance(Location1, Location2):
    R = 6371e3

    lat1 = Location1[1]

    lat2 = Location2[1]

    lon1 = Location1[0]

    lon2 = Location2[0]

    o1 = radians(lat1)
    o2 = radians(lat2)

    do = radians(lat2 - lat1)
    dl = radians(lon2 - lon1)

    a = sin(do / 2) * sin(do / 2) + cos(o1) * cos(o2) * sin(dl / 2) * sin(dl / 2)

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c