#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk           import sent_tokenize, word_tokenize
from nltk.util      import ngrams
from numpy          import mean, std
from csv            import DictReader
from sys            import stdin, stdout
from unicodedata    import normalize as norm

#-----------------------
# annotation stats
#-----------------------

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

#-----------------------
# classify
#-----------------------

def sent_hedge_toks(sentence):
    words = word_tokenize(sentence.decode('utf-8'))
    start = words.index('[')
    words.pop(start)
    end = words.index(']')
    words.pop(end)
    while start < end - 1:
        words[start] += ' ' + words.pop(start + 1)
        end -= 1
    return words[start - 1 : end + 1]

def sent_bigrams(sentence):
    return [bigram for bigram in ngrams(sent_hedge_toks(sentence), 2)]

def bigram_freq(path):
    reader = csv_dict(path)
    bigrams = {}
    for row in reader:
        bs = sent_bigrams(row['segment'])
        for b in bs:
            if b in bigrams:
                bigrams[b] += 1
            else:
                bigrams[b] = 1
    return bigrams

def classify(file_path):
    m = csv_dict(file_path)
    n = sorted(m.items(), key=lambda p: p[1])
    print n

