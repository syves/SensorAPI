from django.db import models

class Occurance(models.Model):
    date        = models.DateField()
    device_id   = models.CharField(max_length=20)
    device_type = models.CharField(max_length=7)
    status      = models.CharField(max_length=7)
