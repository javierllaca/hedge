#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Parse results csv file from CrowdFlower
'''

import csv, sys

def clean_line(line):
	'''
	Return line without <strong> tag
	'''
	return line.replace("<strong>", "").replace("</strong>", "")

def main():
	with sys.stdin as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='\"')
		for row in reader:
			if row['hedge_gold'] == 'yes':
				print "%s\t%s" % (clean_line(row['sentence']), row['orig_hedge'])

if __name__ == "__main__":
	main()
