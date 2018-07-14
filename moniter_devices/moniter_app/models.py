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

class SummaryByDay(models.Model):
    date                 = models.DateField()
    offline_count_by_day = models.IntegerField(default=0)
    online_count_by_day  = models.IntegerField(default=0)

def process(filename):
    with open(filename) as csvfile:
        return set(map(tuple, csv.reader(csvfile)))

def createAnSave(tup):
    rec = Occurance.from_tuple(*(tup))
    return rec.save()
