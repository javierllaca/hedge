#!/usr/bin/python
# -*- coding: utf-8 -*-

from nltk           import sent_tokenize, word_tokenize
from nltk.util      import ngrams
from numpy          import mean, std
from csv            import DictReader, DictWriter
from sys            import argv, stdin, stdout
from random         import randrange
from re             import finditer, match as is_match, sub
from unicodedata    import normalize as norm

def normalize(s):
    """Normalize utf8 characters to their ascii equivalents"""
    return norm('NFD', s.decode('utf8')).encode('ascii', 'ignore')

def join(ls, delim):
    """Return elements in ls separated by delim"""
    return reduce(lambda a, b: a + delim + b, ls)

def choose(n, ls):
    """Return a list of n random elements from ls"""
    if len(ls) <= n:
        return ls
    return [ls.pop(randrange(len(ls))) for i in range(n)]

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

#-----------------------
# append usage
#-----------------------

def hedge_usages(path):
    reader = csv_dict(path)
    hedges = {}
    for row in reader:
        hedges[normalize(row['hedge'])] = (row['usage_a'], row['usage_b'])
    return hedges

def format_entry(line):
    return '\"' + line.replace('\"', '\"\"') + '\"'

def append_usage(path):
    """Append usages to tagged lines"""
    usages = hedge_usages(path)
    for line in stdin:
        line = line.strip()
        a, b = usages[line[:line.index(',')].replace('"', '')]
        print '%s,%s,%s,FALSE,FALSE' % \
                (line.strip(), format_entry(a), format_entry(b))

#-----------------------
# compress csv
#-----------------------

def number_header(header, n):
    return map(lambda s: s + "_%d" % n, header)

def duplicate_header(header, n):
    return reduce(lambda l1, l2: l1 + l2,
            [number_header(header, i) for i in range(1, n + 1)])

def csv_dict(path):
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',', quotechar='\"')
        header = reader.next()
        return header, [row for row in reader]

def group_rows(rows, n):
    """Returns a list of lists made by grouping n elements together"""
    groups, buf, i = [], [], 0
    while len(rows):
        buf.extend([elem for elem in rows.pop(0)])
        i += 1
        if i % n == 0:
            groups.append(buf)
            buf = []
    return groups

def compress_csv(in_path, n, out_path):
    """Compresses n csv rows into one"""
    header, rows = csv_dict(in_path)
    new_header = duplicate_header(header, n)
    new_rows = group_rows(rows, n)
    print new_rows
    writer = csv.writer(open(out_path, 'w'), delimiter=',', quotechar='\"')
    writer.writerow(new_header)
    for row in new_rows:
        writer.writerow(row)

#-----------------------
# distribute gold
#-----------------------

def read_gold(path):
    reader = csv_dict(path)
    gold, ngold = [], []
    for row in reader:
        if row['gold'] == 'TRUE':
            gold.append(row)
        else:
            ngold.append(row)
    return reader.fieldnames, gold, ngold

def write_gold(path, header, rows):
    with open(path, 'w') as csvfile:
        writer = DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

def distribute(n, path):
    """Distributes one row of gold data per n rows and returns the
    header and row data"""
    header, gold, ngold = read_gold(path)
    rows, buf = [], []
    while gold and len(ngold) >= n - 1:
        buf.append(gold.pop(0))
        while len(buf) < n:
            buf.append(ngold.pop(0))
        rows.extend(buf)
        del buf[:]                  # flush buffer
    return header, rows

def distribute_data(in_path, out_path):
    """Evenly distributes gold data"""
    header, rows = distribute(10, in_path)
    write_gold(out_path, header, rows)

#-----------------------
# parse xml
#-----------------------

def parse_xml():
    """Parse xml and print only content enclosed in <post> tags"""
    post = False
    for line in stdin:
        line = line.strip()
        if is_match(r'</post|<quote', line):
            post = False
        elif post and line:
            print sub(r'<img(.*?)/>|<a(.*?)</a>', '', line)
        elif is_match(r'<post|</quote', line):
            post = True

#-----------------------
# select tokens
#-----------------------

def read_token_stream():
    return [line.strip() for line in stdin]

def log_to_file(path, term_frequency):
    """Log results to file"""
    with open(path, 'w') as log_file:
        for term in term_frequency:
            log_file.write('%d\t%s\n' % (term_frequency[term], term))
        log_file.write('------------------------------\n')
        log_file.write('Total matches:\t%d\n' % sum(term_frequency.values()))
        log_file.write('Hedges found:\t%d\n' % len(term_frequency))

def hedge_freq(tokens):
    """Select n random tokens of each hedge"""
    freq = {}
    for token in tokens:
        hedge = token[:token.index(',')].replace('\"', '')
        if hedge in freq:
            freq[hedge] += 1
        else:
            freq[hedge] = 1
    return freq

def select_tokens(n):
    tokens = read_token_stream()
    for choice in choose(n, tokens):
        print choice
    log_to_file('out.txt', hedge_freq(tokens))

