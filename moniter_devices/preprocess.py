#!/usr/bin/env python
import os
import django
import sys
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moniter_devices.settings")
django.setup()
from moniter_app.models import process

local_path = "/Users/syves/github.com/syves"
reports_dir = "{}/Assignment/moniter_devices/reports/".format(local_path)
filepath = "{}/Assignment/moniter_devices/reports/report.csv".format(local_path)
target = "{}/Assignment/moniter_devices/processed/clean_data.json".format(local_path)

for file in os.listdir(reports_dir):
    with open(target, 'w') as outfile:
        print(json.dumps(list(process(filepath))), file=outfile)

#If I knew how the incoming reports were named I would create an output file for each report.
