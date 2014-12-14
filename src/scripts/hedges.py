#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Parse results csv file from CrowdFlower"""

from csv import DictReader
from sys import stdin, argv
from numpy import mean, std

def main():
	with stdin as csvfile:
		reader = DictReader(csvfile, delimiter=',', quotechar='\"')
		confidence = {}
		for row in reader:
			hedge = row['orig_hedge']
			if hedge in confidence:
				confidence[hedge].append(float(row['hedge:confidence']))
			else:
				confidence[hedge] = [float(row['hedge:confidence'])]

		hedges = [(hedge, mean(confidence[hedge]), std(confidence[hedge]), len(confidence[hedge])) 
				for hedge in confidence]

		print '%-20s %-20s %-20s %-20s' % ('hedge', 'average', 'std. dev.', 'instances')
		print '-' * 80
		for hedge in sorted(hedges, key=lambda c: c[1], reverse=True):
			print '%-20s %-20f %-20f %-20d' % hedge

if __name__ == "__main__":
	main()
