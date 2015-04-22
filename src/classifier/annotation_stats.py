#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import stdin

def annotation_stats():
    """Print stats for annotations"""
    frequency = {\
            'HREL'  : 0, \
            'HPROP' : 0, \
            'NH'    : 0}
    for line in stdin:
        belief_type = line.split('\t')[-1].strip()
        if belief_type in frequency:
            frequency[belief_type] += 1
    for key in frequency:
        print '%s:\t%d' % (key, frequency[key])
    print '-' * 20
    print 'Total:\t%d' % sum([frequency[i] for i in frequency])
