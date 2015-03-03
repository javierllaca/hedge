#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
from sys import argv, stdin, stdout

def number_header(header, n):
    return map(lambda s: s + "_%d" % n, header)

def duplicate_header(header, n):
    return reduce(lambda l1, l2: l1 + l2,
            [number_header(header, i) for i in range(1, n + 1)])

def read_csv(path):
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

def main(path, n):
    """Compresses n csv rows into one"""
    header, rows = read_csv(path)
    new_header = duplicate_header(header, n)
    new_rows = group_rows(rows, n)
    print new_rows
    writer = csv.writer(open('temp.csv', 'w'), delimiter=',', quotechar='\"')
    writer.writerow(new_header)
    for row in new_rows:
        writer.writerow(row)

if __name__ == "__main__" and len(argv) == 3:
    main(argv[1], int(argv[2]))
