#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Append usages to tagged lines"""

from csv import DictReader
from sys import argv, stdin
import unicodedata

def normalize(s):
    """Normalizes utf8 characters to their ascii equivalents"""
    return unicodedata.normalize(
            'NFD', s.decode('utf8')).encode('ascii', 'ignore')

def hedge_dict(path):
    with open(path, 'r') as hedgefile:
        reader = DictReader(hedgefile, delimiter=',', quotechar='\"')
        hedges = {}
        for row in reader:
            hedges[normalize(row['hedge'])] = row
        return hedges

def format_entry(line):
    return '\"' + line.replace('\"', '\"\"') + '\"'

def main(path):
    hedges = hedge_dict(path)
    for line in stdin:
        row = hedges[line[:line.index(',')].replace('"', '')]
        print '%s,%s,%s' % (line.strip(), 
                format_entry(row['usage_a']), format_entry(row['usage_b']))

if __name__ == '__main__':
    main(argv[1])
