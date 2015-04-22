#!/usr/bin/python
# -*- coding: utf-8 -*-

from csv            import DictReader
from nltk           import sent_tokenize, word_tokenize
from nltk.util      import ngrams
from sys            import argv

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

def hedge_tokens(path):
    with open(path, 'r') as csv_file:
        reader = DictReader(csv_file, delimiter='\t', quotechar='\"')
        return [(row['segment'], row['proposition'], row['belief_type']) 
                for row in reader]

def type_to_bool(t):
    return t != 'NH'

def bigram_sense_pairs(tokens):
    return [(b, type_to_bool(t)) 
            for s, p, t in tokens
            for b in sent_bigrams(s)]

def bigram_table(bigram_sense_pairs):
    table = {}
    for bigram, sense in bigram_sense_pairs:
        if bigram not in table:
            table[bigram] = {}
        if sense in table[bigram]:
            table[bigram][sense] += 1
        else:
            table[bigram][sense] = 1
    return table

def classify(file_path):
    table = bigram_table(bigram_sense_pairs(hedge_tokens(file_path)))
    print table
    print '%d unique bigrams' % len(table)

if __name__ == '__main__':
    if len(argv) == 2:
        classify(argv[1])
    else:
        print 'Usage: %s <in>' % argv[0]

