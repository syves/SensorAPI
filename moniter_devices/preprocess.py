#!/usr/bin/env python
import os
import sys

import models.py

filepath = "/Users/syves/github.com/syves/Assignment/moniter_devices/report.csv"

#maybe split these jobs into two files...
#save results of preprocess to anotther file.
for tup in process(filepath): s = Occurance.from_tuple(*(tup)); s.save()
