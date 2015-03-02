#!/usr/bin/python
# -*- coding: utf-8 -*-

from csv import DictReader
from sys import stdin, argv

def main():
    """Parse results csv file from CrowdFlower"""
	with stdin as csvfile:
		reader = DictReader(csvfile, delimiter=',', quotechar='\"')
		confidence = {}
		for row in reader:
			contributor = int(row['_worker_id'])
			if contributor not in confidence:
				confidence[contributor] = [float(row['_trust']), 1]
			else:
				confidence[contributor][1] += 1

		contributors = [(contributor, confidence[contributor][0], confidence[contributor][1]) 
				for contributor in confidence]

		print '%-20s %-20s %-20s' % ('contributor id', 'confidence', 'judgements')
		print '-' * 60
		for contributor in sorted(contributors, key=lambda c: c[1], reverse=True):
			print '%-20d %-20f %-20d' % contributor

if __name__ == "__main__":
	main()
