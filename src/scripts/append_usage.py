#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Append definitions to tagged lines
'''

import os, re, sys, unicodedata

def normalize(s):
	return unicodedata.normalize('NFD', s.decode('utf8')).encode('ascii', 'ignore')

def definition_map(path):
	definition_map = dict()
	for line in open(path, 'r'):
		tokens = re.split('\\t+', line)
		term = tokens[0]
		defs = []
		for i in range(1, len(tokens)):
			defs.append(tokens[i].strip())
		definition_map[term] = defs
		definition_map[normalize(term)] = defs
	return definition_map

'''
ArrayList<String> definitions = new ArrayList<String>();
for (int i = 1; i < tokens.length; i++) {
	definitions.add(tagLine(tokens[i], term, this.tag));
}

tagLine(String line, String query, String label) {
	regex = normalize(query) + "|" + normalize(capitalize(query));
	matcher = Pattern.compile(regex).matcher(PatternUtils.normalizeEncoding(line));
	if (matcher.find()) {
		return tag(line, tag, matcher.group(), matcher.start(), matcher.end());
	}
	return line;
}
'''

def traverse(path, function):
	path = os.path.abspath(path)
	if os.path.isfile(path):
		return eval(function)(path)
	else:
		total = dict()
		for f in os.listdir(path):
			total = dict(total.items() + traverse(path + '/' + f, function).items())
		return total

def regex(collection, separator):
	s = "\\b(" + collection[0]
	for i in range(1, len(collection)):
		s += separator + collection[i]
	return s + ")\\b"

path = sys.argv[1]
hedge_map = traverse(path, 'definition_map')

for line in sys.stdin:
	print line.rstrip(),
	definitions = hedge_map[line[:line.index(',')].replace('\"', '')]
	if definitions:
		for definition in definitions:
			sys.stdout.write(',\"' + definition.replace('\"', '\"\"') + '\"')
	sys.stdout.write('\n')
