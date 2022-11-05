from django.db import models


class Delivery(models.Model):

    date = models.DateTimeField()
    address = models.CharField(max_length=100, default='')
    lat = models.FloatField()
    lon = models.FloatField()
    fee = models.IntegerField()


class FeeRequest(models.Model):

    drop_off_date = models.DateTimeField()
    drop_off_address = models.CharField(max_length=100, default='')


