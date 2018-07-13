from django.shortcuts import get_object_or_404, render
from django.db.models import Count
import datetime

from .models import Occurance
from operator import itemgetter

def percentage_change(old, new):
    if old == 0:
        return 'n/a'
    return "{:.1f} %".format((new - old) / old * 100)

def get_count_by_day(date):
    l = (Occurance.objects
        .values('device_id')
        .filter(date=date)
        .annotate(dcount=Count('device_id')))
    return {elem['device_id']: elem['dcount']  for elem in l}

def index(request):
    occurances = Occurance.objects.values('device_id').distinct()
    return render(request, 'moniter_app/index.html', {'occurances': occurances})

def date(request, date_string):
    date = datetime.datetime.strptime(date_string, '%Y-%m-%d').date()
    selected_date_data_set = list(get_count_by_day(date).items())
    selected_date_data_set.sort(key=itemgetter(1), reverse=True)

    delta_date_data_set = get_count_by_day(date - datetime.timedelta(days=7))
    popular = [{'device_id': device_id,
                'count': count,
                'change': percentage_change(delta_date_data_set.get(device_id, 0), count),
                'old_count': delta_date_data_set.get(device_id, 0)}
               for device_id, count in selected_date_data_set[:10]]
    return render(request, 'moniter_app/date.html', {'popular': popular})

def device(request, device_type, status):
    device = device_type
    occurances = Occurance.objects.values('date').filter(device_type=device_type,status=status).annotate(dcount=Count('date'))
    return render(request, 'moniter_app/device.html', {'occurances': occurances})
