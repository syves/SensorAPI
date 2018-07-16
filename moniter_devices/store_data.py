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

local_path = "/Users/syves/github.com/syves"
cleaned_data_dir = "{}/Assignment/moniter_devices/processed/".format(local_path)
cleaned_data = "{}/Assignment/moniter_devices/processed/clean_data.json".format(local_path)

for file in os.listdir(cleaned_data_dir):
    with open(cleaned_data, 'r') as input:
        data =  json.load(input)
        for tup in data:
            print(tup)
            s = Occurance.from_tuple(*(tup)); s.save()
