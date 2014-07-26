#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Select n random tokens of each hedge
'''

import random, sys

def choose(n, a):
	'''
	Choose n random elements from list a
	'''
	choices = []
	size = n if len(a) > n else len(a)
	for i in range(0, size):
		index = random.randrange(len(a))
		choice = a.pop(index)
		choices.append(choice)
	return choices

def log_to_file(filename, term_frequency):
	log_file = open(filename, 'w')
	total_matches = hedges_found = 0

	for (term,count) in term_frequency:
		log_file.write(str(count) + "\t" + term + "\n")
		total_matches += count
		hedges_found += 1

	log_file.write("------------------------------\n")
	log_file.write("Total matches:\t" + str(total_matches) + "\n")
	log_file.write("Hedges found:\t" + str(hedges_found) + "\n")
	log_file.close()

def main(argv):
	number = int(argv[1])
	
	count = 0
	current = "" 
	ls = []
	term_frequency = []

	for line in sys.stdin:
		term = line[:line.index(',')].replace('\"', '')
		if term != current:
			term_frequency.append((current, count))
			for choice in choose(number, ls):
				print choice
			current = term
			count = 1
			ls = [line.strip()]
		else:
			count += 1
			ls.append(line.strip())
	term_frequency.append((current, count))
	for choice in choose(number, ls):
		print choice

	log_to_file(argv[2], term_frequency)

if __name__ == "__main__":
	main(sys.argv)
