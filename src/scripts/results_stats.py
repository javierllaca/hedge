#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Parse results csv file from CrowdFlower
'''

import csv, sys

def main():
	with sys.stdin as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='\"')
		gold = hedge = prob_sum = rownum = 0
		for row in reader:
			if row['hedge'] == 'yes':
				hedge += 1
			if row['hedge_gold'] == 'yes':
				gold += 1
			prob_sum += float(row['hedge:confidence'])
			rownum += 1
		print "Hedges: %d / %d\nGold: %d\nAverage confidence: %f" % \
				(hedge, rownum, gold, prob_sum / float(rownum))

if __name__ == "__main__":
	main()
