#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk           import sent_tokenize, word_tokenize
from nltk.util      import ngrams
from numpy          import mean, std
from csv            import DictReader
from sys            import stdin, stdout
from unicodedata    import normalize as norm

def normalize(s):
    """Normalize utf8 characters to their ascii equivalents"""
    return norm('NFD', s.decode('utf8')).encode('ascii', 'ignore')

def join(ls, delim):
    """Return elements in ls separated by delim"""
    return reduce(lambda a, b: a + delim + b, ls)

def csv_dict(path):
    """Return a dictionary wrapping contents of csv file in path"""
    with open(path, 'r') as hedgefile:
        return DictReader(hedgefile, delimiter='\t', quotechar='\"')

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

#-----------------------
# decompress
#-----------------------

def load_hits(path):
    reader = csv_dict(path)
    hits = {}
    for row in reader:
        hit_id = row['HITId']
        if hit_id in hits:
            hits[hit_id].append(row)
        else:
            hits[hit_id] = [row]
    return hits

def units(hit, n):
    units = {}
    for task in hit: # hit
        for i in range(1, n + 1):
            unit = (task['Input.hedge_%d' % i], \
                    task['Input.sentence_%d' % i])
            val = (task['WorkerId'], \
                    task['Answer.hedge_judgement_%d' % i])
            if unit in units:
                units[unit].append(val)
            else:
                units[unit] = [val]
    res = []
    for unit in units:
        judgements = {\
                'TRUE'  : 0, \
                'FALSE' : 0, \
                ''      : 0}          # no judgement
        for judgement in units[unit]:
            judgements[judgement[1]] += 1
        res.append((unit, judgements))
    return res

def is_fuzzy(unit):
    unit, judgements = unit
    yes, no = judgements['TRUE'], judgements['FALSE']
    return abs(yes - no) <= 1

def untag(line):
    return line.replace('<strong>', '[').replace('</strong>', ']')

def hedge_types(path):
    reader = csv_dict(path)
    hedges = {}
    for row in reader:
        hedges[normalize(row['hedge']).strip()] = row['hedge_type']
    return hedges

def print_list(ls):
    hedge_types = hedge_types('../../database/hedges.csv')
    for elem in ls:
        unit, judgement = elem
        hedge, sent = unit
        yes, no = judgement['TRUE'], judgement['FALSE']
        if yes > no:
            print '%s\t%s\t%s' % (untag(sent), hedge, hedge_types[hedge])
        else:
            print '%s\t%s\tNH' % (untag(sent), hedge)

def decompress(path, n):
    hits = load_hits(path)
    good, fuzzy = [], []
    for hit in hits:
        us = units(hits[hit], n)
        good.extend([u for u in us if not is_fuzzy(u)])
        fuzzy.extend([u for u in us if is_fuzzy(u)])
    print_list(good)
