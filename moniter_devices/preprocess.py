#!/usr/bin/env python
import csv
import json
import os

base_path = os.path.dirname(os.path.realpath(__file__))
filepath = os.path.join(base_path, 'reports', 'report.csv')
target = os.path.join(base_path, 'processed', 'clean_data.json')

def process(filename):
    with open(filename) as csvfile:
        return set(map(tuple, csv.reader(csvfile)))

with open(target, 'w') as outfile:
    print(json.dumps(list(process(filepath))), file=outfile)
