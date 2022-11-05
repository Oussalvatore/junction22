from rest_framework import serializers
from .models import Delivery, FeeRequest


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ['id', 'date', 'address', 'lat', 'lon', 'fee']


class FeeRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeeRequest
        fields = ['id', 'drop_off_date', 'drop_off_address']