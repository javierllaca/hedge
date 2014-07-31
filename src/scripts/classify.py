#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re, sys, unicodedata

def normalize(s):
	return unicodedata.normalize('NFD', s.decode('utf8')).encode('ascii', 'ignore')

def traverse(path):
	term_list = []
	term_map = dict()
	for f in os.listdir(path):
		for line in open(os.path.abspath(path) + '/' + f, 'r'):
			term = line.split('\t')[0].strip()
			term_map[normalize(term)] = term
			term_list.append(normalize(term))
	return (term_list, term_map)

def regex(collection, separator):
	s = "\\b(" + collection[0]
	for i in range(1, len(collection)):
		s += separator + collection[i]
	return s + ")\\b"

def main(argv):
	res = traverse(argv[1])
	tag = argv[2]
	pattern = regex(res[0], '|')
	for line in sys.stdin:
		tokens = line.split('\t')
		if re.match(pattern, tokens[1]):
			print tokens[0] + '\t',
			print res[1][tokens[1].strip()] + '\t',
			print tag
		else:
			print line.strip()

if __name__ == '__main__':
	main(sys.argv)
