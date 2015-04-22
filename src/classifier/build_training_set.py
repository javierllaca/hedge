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

def tokens(path):
    with open(path, 'r') as csv_file:
        reader = DictReader(csv_file, delimiter='\t', quotechar='\"')
        return [(row['segment'], row['proposition'], row['belief_type']) 
                for row in reader]

def bigram_freq(path):
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
    print tokens(file_path)

if __name__ == '__main__':
    if len(argv) == 2:
        classify(argv[1])
    else:
        print 'Usage: %s <in>' % argv[0]

