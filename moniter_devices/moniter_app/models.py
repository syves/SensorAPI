from django.db import models
import datetime
import calendar
import csv

class Occurance(models.Model):
    date    = models.DateField()
    device_id   = models.CharField(max_length=20)
    device_type = models.CharField(max_length=7)
    status      = models.CharField(max_length=7)

    @staticmethod
    def from_tuple(timestamp, device_id, device_type, status):
         return Occurance(
            date=datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ').date(),
            device_id=device_id,
            device_type=device_type,
            status=status)

def process(filename):
    with open(filename) as csvfile:
        return set(map(tuple, csv.reader(csvfile)))
