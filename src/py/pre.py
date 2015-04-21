#!/usr/bin/python
# -*- coding: utf-8 -*-

from csv            import DictReader, DictWriter
from sys            import stdin, stdout
from random         import randrange
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
# select tokens
#-----------------------

def choose(n, ls):
    """Return a list of n random elements from ls"""
    if len(ls) <= n:
        return ls
    return [ls.pop(randrange(len(ls))) for i in range(n)]

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

