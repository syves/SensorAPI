#!/usr/bin/env python
import os
import django
import sys
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moniter_devices.settings")
django.setup()
from moniter_app.models import process

reports_dir = "/Users/syves/github.com/syves/Assignment/moniter_devices/reports/"
filepath = "/Users/syves/github.com/syves/Assignment/moniter_devices/reports/report.csv"
target = "/Users/syves/github.com/syves/Assignment/moniter_devices/processed/clean_data.json"

for file in os.listdir(reports_dir):
    with open(target, 'w') as outfile:
        print(json.dumps(list(process(filepath))), file=outfile)

#If I knew how the incoming reports were named I would create an output file for each report.
