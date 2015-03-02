#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, re, unicodedata
from sys import argv, stdin

def normalize(string):
    """Returns the string with non-ASCII characters normalized to their ASCII
    equivalents
    """
    return unicodedata.normalize('NFD', string.decode('utf8')).encode('ascii', 'ignore')

def traverse(path):
    """Returns a (list, dictionary) pair with contents of files in path
    - List contains all normalized terms in files
    - Dictionary contains a mapping of the form:
      normalized spelling -> actual spelling
    """
    term_list = []
    term_map = dict()
    for f in os.listdir(path):
        for line in open(os.path.abspath(path) + '/' + f, 'r'):
            term = line.split('\t')[0].strip()
            term_map[normalize(term)] = term
            term_list.append(normalize(term))
    return (term_list, term_map)

def join(ls, separator):
    """Returns a string with all elements in ls separated by separator"""
    s = "\\b(" + ls[0]
    for i in range(1, len(ls)):
        s += separator + ls[i]
    return s + ")\\b"

def main(argv):
    temp = traverse(argv[1])
    term_list = temp[0]
    term_map = temp[1]

    tag = argv[2]
    regex = join(term_list, '|')

    for line in stdin:
        line = line.strip()
        tokens = line.split('\t')
        if (len(tokens) == 3 and tokens[2] == 'NH') or not re.match(regex, tokens[1]):
            print line.strip()
        else :
            print tokens[0] + '\t',
            print term_map[tokens[1]] + '\t',
            print tag

if __name__ == '__main__':
    main(argv)
