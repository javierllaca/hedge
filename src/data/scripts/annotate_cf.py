#!/usr/bin/python
# -*- coding: utf-8 -*-

from csv            import DictReader, writer as csv_writer
from sys            import stdin, argv
from unicodedata    import normalize as norm

def normalize(s):
    """Normalize utf8 characters to their ascii equivalents"""
    return norm('NFD', s.decode('utf8')).encode('ascii', 'ignore')

def change_tag(line):
    return line.replace("<strong>", "[").replace("</strong>", "]")

def load_units(path):
    with open(path, 'r') as csv_file:
        reader = DictReader(csv_file, delimiter=',', quotechar='\"')
        return [(row['orig_hedge'].strip(),
                 row['sentence'],
                 row['hedge'],
                 row['hedge:confidence'])
                 for row in reader]

def load_hedge_types(path):
    with open(path, 'r') as csv_file:
        reader = DictReader(csv_file, delimiter=',', quotechar='\"')
        hedges = {}
        for row in reader:
            hedges[normalize(row['hedge']).strip()] = row['hedge_type']
        return hedges

def parse_results(in_path, out_path, threshold, hedge_path):
    """Parse results csv file from CrowdFlower"""
    hedge_types = load_hedge_types(hedge_path)
    hits = load_units(in_path)
    with open(out_path, 'w') as csv_file:
        writer = csv_writer(csv_file, delimiter='\t', quotechar='\"')
        writer.writerow(['segment', 'proposition', 'belief_type'])
        for hedge, sent, judgement, confidence in hits:
            if confidence > threshold:
                if judgement == 'yes':
                    writer.writerow([change_tag(sent), hedge, hedge_types[hedge]])
                else:
                    writer.writerow([change_tag(sent), hedge, 'NH'])

if __name__ == "__main__":
    if len(argv) == 5:
        parse_results(argv[1], argv[2], float(argv[3]), argv[4])
    else:
        print 'Usage: python %s <in> <out> <confidence> <hedges>' % argv[0]

