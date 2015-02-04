#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Append definitions to tagged lines"""

import os, re, sys, unicodedata

def normalize(s):
	"""Return encoding-normalized string
	Change utf8 characters to their ascii equivalents"""
	return unicodedata.normalize('NFD', s.decode('utf8')).encode('ascii', 'ignore')

def definition_map(path):
	"""Returns a dictionary with terms as keys and its usages as values
	From file specified by path"""
	definition_map = {}
	for line in open(path, 'r'):
		tokens = re.split('\\t+', line.strip())
		term = tokens[0]
		definitions = []
		for i in range(1, len(tokens)):
			definitions.append(tokens[i].strip())
		definition_map[normalize(term)] = definitions
	return definition_map

def traverse(path, function):
	"""Recursively traverses a directory with a specified function
	- If path is a file, calls function on path 
	- Otherwise, returns all traversals of contents of path"""
	path = os.path.abspath(path)
	if os.path.isfile(path):
		return eval(function)(path)
	else:
		total = {}
		for f in os.listdir(path):
			total = dict(total.items() + traverse(path + '/' + f, function).items())
		return total

def main(argv):
	path = argv[1]
	hedge_map = traverse(path, 'definition_map')

	for line in sys.stdin:
		print line.rstrip(),
		definitions = hedge_map[line[:line.index(',')].replace('\"', '')]
		if definitions:
			for definition in definitions:
				sys.stdout.write(',\"' + definition.replace('\"', '\"\"') + '\"')
		sys.stdout.write('\n')

if __name__ == '__main__':
	main(sys.argv)
