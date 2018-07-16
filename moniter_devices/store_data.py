#!/usr/bin/env python
import os
import django
import sys
import readline # optional, will allow Up/Down/History in the console
import code
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moniter_devices.settings")
django.setup()
from moniter_app.models import Occurance

variables = globals().copy()
variables.update(locals())
shell = code.InteractiveConsole(variables)
#shell.interact()

cleaned_data_dir = "/Users/syves/github.com/syves/Assignment/moniter_devices/processed/"
cleaned_data = "/Users/syves/github.com/syves/Assignment/moniter_devices/processed/clean_data.json"

mydata = "foo"

for file in os.listdir(cleaned_data_dir):

    with open(cleaned_data, 'r') as input:
        data =  json.load(input)
        for tup in data:
            print(tup)
            #Occurance.from_tuple(*(tup)); s.save()
#save to the database somehow.
