#!/usr/bin/python
# -*- coding: utf-8 -*-

from csv import DictReader
from sys import stdin, argv

def clean_line(line):
	"""Return line without <strong> tag"""
	return line.replace("<strong>", "").replace("</strong>", "")

def main(argv):
    """Parse results csv file from CrowdFlower"""
	fuzzy = []
	with stdin as csvfile:
		reader = DictReader(csvfile, delimiter=',', quotechar='\"')
		threshold = float(argv[1])
		for row in reader:
			if float(row['hedge:confidence']) > threshold:
				sentence = clean_line(row['sentence'])
				hedge = row['orig_hedge'] 
				if row['hedge'] == 'no':
					#s = 3
					print "%s\t%s\tNH" % (sentence, hedge)
				else:
					#s = 3
					print "%s\t%s" % (sentence, hedge)
			else:
				fuzzy.append(row)
	return fuzzy

if __name__ == "__main__":
	main(argv)
