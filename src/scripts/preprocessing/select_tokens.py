#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import randrange
from sys import argv, stdin

def choose(n, ls):
    """Choose n random elements from list ls"""
    if len(ls) <= n:
        return ls
    choices = []
    for i in range(n):
        index = randrange(len(ls))
        choices.append(ls.pop(index))
    return choices

def log_to_file(filename, term_frequency):
    """Log results to file"""
    log_file = open(filename, 'w')
    total_matches = hedges_found = 0
    for (term,count) in term_frequency:
        if count > 0:
            log_file.write(str(count) + '\t' + term + '\n')
            total_matches += count
            hedges_found += 1
    log_file.write('------------------------------\n')
    log_file.write('Total matches:\t' + str(total_matches) + '\n')
    log_file.write('Hedges found:\t' + str(hedges_found) + '\n')
    log_file.close()

def main(argv):
    """Select n random tokens of each hedge"""
    number = int(argv[1])
    count = 0
    current = "" 
    ls = []
    term_frequency = []
    for line in stdin:
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

if __name__ == '__main__':
    main(argv)
