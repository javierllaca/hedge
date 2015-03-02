#!/usr/bin/python
# -*- coding: utf-8 -*-

from csv import DictReader
from sys import stdin
from numpy import mean, median, std

def analyze(stream):
	with stream as csvfile:
		reader = DictReader(csvfile, delimiter=',', quotechar='\"')
		hedges = non_hedges = 0
		confidence = []
		for row in reader:
			if row['hedge'] == 'yes':
				hedges += 1
			else:
				non_hedges += 1
			confidence.append(float(row['hedge:confidence']))
		return hedges, non_hedges, confidence
	
def main():
    """Parse results csv file from CrowdFlower"""

	hedges, non_hedges, confidence = analyze(stdin)

	print ('*' * 5) + 'Distribution' + ('*' * 5) + '\n'
	print '%-15s %d' % ('Hedges', hedges)
	print '%-15s %d' % ('Non-Hedges', non_hedges)

	print '\n' + ('*' * 5) + 'Confidence' + ('*' * 5) + '\n'
	print '%-15s %f' % ('Mean', mean(confidence))
	print '%-15s %f' % ('Median', median(confidence))
	print '%-15s %f' % ('Std. Dev.', std(confidence))
	print '%-15s %f' % ('Max', max(confidence))
	print '%-15s %f' % ('Min', min(confidence))

if __name__ == "__main__":
    main()
