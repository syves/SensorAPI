from django.shortcuts import get_object_or_404, render
from django.db.models import Count

from .models import Occurance

def index(request):
    occurances = Occurance.objects.filter(status='online', device_id='bb10684d')[:30]
    return render(request, 'moniter_app/index.html', {'occurances': occurances})

def date(request, date):
    #occurances2 = Occurance.objects.order_by('datetime')[:10]
    occurances = Occurance.objects.all()
    return render(request, 'moniter_app/date.html', {'occurances': occurances})

def device(request, device_id, status):
    #todays date -30 time delta?
    id = device_id
    stat = status
    occurances = Occurance.objects.values('date').filter(device_id=device_id,status=status).annotate(dcount=Count('date'))
    return render(request, 'moniter_app/device.html', {'occurances': occurances})
