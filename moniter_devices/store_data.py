#!/usr/bin/env python
import os
import django
import sys
import json
from django.db import models

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moniter_devices.settings")
django.setup()
from moniter_app.models import Occurance

from django.apps import apps
ap=apps.get_model('moniter_app','Occurance')

cleaned_data_dir = "/Users/syves/github.com/syves/Assignment/moniter_devices/processed/"
cleaned_data = "/Users/syves/github.com/syves/Assignment/moniter_devices/processed/clean_data.json"

for file in os.listdir(cleaned_data_dir):
    with open(cleaned_data, 'r') as input:
        data =  json.load(input)
        for tup in data:
            print(tup)
            s = Occurance.from_tuple(*(tup)); s.save()
