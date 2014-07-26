#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Parse xml and print only content enclosed in <post> tags
'''

import re, sys

def clean_line(line):
	'''
	Return line without <img> and <a> tags
	'''
	clean = line
	regex = "<img(.*?)/>" + "|" + "<a(.*?)</a>"	
	matches = re.finditer(regex, clean)
	for match in matches:
		clean = clean.replace(match.group(), "")
	return clean

def main():
	post = False
	for line in sys.stdin:
		if any(x in line for x in ["</post", "<quote"]):
			post = False
		elif post and line.strip():
			clean = clean_line(line).strip()
			if clean:
				print clean
		elif any(x in line for x in ["<post", "</quote"]):
			post = True

if __name__ == "__main__":
	main()
