from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Moniter Devices.")

def date(request, datetime):
    return HttpResponse("You're looking at question %s." % datetime)

def device(request, device_type, status, ):
    response = "You're looking at device by status over 30 days %s."
    return HttpResponse(response % device_type % status)
