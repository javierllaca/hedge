#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Parse results csv file from CrowdFlower"""

from csv import DictReader
from sys import stdin, argv

def frequency(stream):
	frequency = {'true': {'yes': 0, 'no': 0}, 'false': {'yes': 0, 'no': 0}}
	with stream as csvfile:
		reader = DictReader(csvfile, delimiter=',', quotechar='\"')
		for row in reader:
			frequency[row['_golden']][row['hedge']] += 1
	return frequency

def hedge_ratio(frequency):
	return float(frequency['yes']) / float(frequency['no'])

if __name__ == "__main__":
	val = {'true': 'test', 'false': 'contributor'}
	freq_maps = frequency(stdin)
	print '%-15s%s' % ('domain', 'hedge / non-hedge')
	print '-' * 35
	for f in freq_maps:
		print '%-15s%f' % (val[f], hedge_ratio(freq_maps[f]))
