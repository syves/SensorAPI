#!/usr/bin/env python
import os
import sys

import models.py

filepath = "/Users/syves/github.com/syves/Assignment/moniter_devices/report.csv"

def createAnSave(tup):
    rec = Occurance.from_tuple(*(tup))
    rec.save()

for tup in process(filepath): s = Occurance.from_tuple(*(tup)); s.save()

#currently seeding the database in the interactive shell

# $ from moniter_app.models import Occurance, SummaryByDay, process, createAnSave

# $ import datetime

#only do this step if not in scope, this might not be necesary in models.py
# $ def createAnSave(tup): rec = Occurance.from_tuple(*(tup)); return rec.save()

# $ for tup in process("report.csv"): s = Occurance.from_tuple(*(tup)); s.save()

#check for success
#$ Occurance.objects.all().count()
