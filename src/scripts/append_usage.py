#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Append definitions to tagged lines
'''

import os, re, sys, unicodedata

def normalize(s):
	'''
	Return encoding-normalized string
	Change utf8 characters to their ascii equivalents
	'''
	return unicodedata.normalize('NFD', s.decode('utf8')).encode('ascii', 'ignore')

def tag_line(line, query, label):
	'''
	Return line with first instance of query tagged with label
	'''
	regex = normalize(query) + '|' + normalize(query.capitalize());
	match = re.search(regex, normalize(line));
	if match:
		before = line[:match.start()]
		middle = "<" + label + ">" + match.group() + "</" + label + ">"
		after = line[match.end():]
		return before + middle + after
	return line;

def definition_map(path):
	'''
	Returns a dictionary with terms as keys and its usages as values
	From file specified by path
	'''
	definition_map = dict()
	for line in open(path, 'r'):
		tokens = re.split('\\t+', line)
		term = tokens[0]
		definitions = []
		for i in range(1, len(tokens)):
			definition = tokens[i].strip()
			definitions.append(tag_line(definition, term, "strong"))
		definition_map[term] = definitions
		definition_map[normalize(term)] = definitions
	return definition_map

def traverse(path, function):
	'''
	Recursively traverse a directory with a specified function
	Calls function on path if path is a file
	Traverses contents of path otherwise
	Returns combined values of calls to function
	'''
	path = os.path.abspath(path)
	if os.path.isfile(path):
		return eval(function)(path)
	else:
		total = dict()
		for f in os.listdir(path):
			total = dict(total.items() + traverse(path + '/' + f, function).items())
		return total

def regex(ls, separator):
	'''
	Returns a regex formed by combining elements in collection
	'''
	s = "\\b(" + ls[0]
	for i in range(1, len(ls)):
		s += separator + ls[i]
	return s + ")\\b"

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

if __name__ == "__main__":
	main(sys.argv)
