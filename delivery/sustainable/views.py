from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Delivery
from .serializers import DeliverySerializer, FeeRequestSerializer
from .utils import *

from .parameters import VENUE_ADDRESS

@csrf_exempt
def get_estimates(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeeRequestSerializer(data=data)
        if serializer.is_valid():
            response = get_delivery_fee(VENUE_ADDRESS, data["drop_off_address"])
            response_data = response.json()
            if response.status_code == 200:
                lat_d = response_data['dropoff']['location']['coordinates']['lat']
                lon_d = response_data['dropoff']['location']['coordinates']['lon']
                same_dropoff_count = 0
                time_classified_deliveries = {}
                deliveries = Delivery.objects.all()
                for d in deliveries:
                    lat = d.lat
                    lon = d.lon
                    distance = compute_distance((lat_d, lon_d), (lat, lon))
                    if distance <= DISTANCE_THRESHOLD:
                        if str(d.date) in time_classified_deliveries:
                            time_classified_deliveries[str(d.date)].append(d)
                        else:
                            time_classified_deliveries[str(d.date)] = [d]
                to_return = {}
                to_return["fee"] = response_data['fee']['amount']
                to_return["cheaper_fees"] = []
                for date in time_classified_deliveries:
                    tmp = {
                            "date":date,
                            "fee": (response_data['fee']['amount'] * (1 + INTEREST)) /
                                  (len(time_classified_deliveries[date]) + 1)
                           }
                    to_return["cheaper_fees"].append(tmp)

                return JsonResponse(to_return, status=200)
            else:
                return JsonResponse({"error": response.json().error_code}, status=response.code)


@csrf_exempt
def delivery_list(request):

    if request.method == 'GET':
        deliveries = Delivery.objects.all()
        serializer = DeliverySerializer(deliveries, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        response = send_delivery_request(VENUE_ADDRESS, data['address'], data['date'])
        if response.status_code == 201:
            data['lat'] = response.json()['dropoff']['location']['coordinates']['lat']
            data['lon'] = response.json()['dropoff']['location']['coordinates']['lon']
            if "fee" not in data:
                data['fee'] = response.json()['price']['amount']

            serializer = DeliverySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        else:
            return JsonResponse(response.json(), status=response.status_code)


@csrf_exempt
def delivery_detail(request, pk):

    try:
        delivery = Delivery.objects.get(pk=pk)
    except Delivery.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DeliverySerializer(delivery)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DeliverySerializer(delivery, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        delivery.delete()
        return HttpResponse(status=204)