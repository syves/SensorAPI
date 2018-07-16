#!/usr/bin/env python
import datetime
import json
import os

import django
from django.db import models

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moniter_devices.settings")
django.setup()
from moniter_app.models import Occurance

local_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
cleaned_data_dir = os.path.join(local_path, 'moniter_devices', 'processed')
cleaned_data = os.path.join(cleaned_data_dir, 'clean_data.json')

for file in os.listdir(cleaned_data_dir):
    with open(cleaned_data, 'r') as input:
        data = json.load(input)
        for timestamp, device_id, device_type, status in data:
            s = Occurance(
                date=datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ').date(),
                device_id=device_id,
                device_type=device_type,
                status=status
            )
            s.save()
