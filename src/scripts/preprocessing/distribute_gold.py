#!/usr/bin/python
# -*- coding: utf-8 -*-

from csv import DictReader, DictWriter
from sys import argv, stdin

def read_gold(path):
    with open(path, 'r') as csv_file:
        reader = DictReader(csv_file, delimiter=',', quotechar='\"')
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
    rows = []
    i = 0
    for g_t in gold:
        rows.append(g_t)
        for j in range(n - 1):
            if i < len(ngold):
                rows.append(ngold[i])
                i += 1
    return header, rows

def main(in_path, out_path):
    """Evenly distributes gold data"""
    header, rows = distribute(10, in_path)
    write_gold(out_path, header, rows)

if __name__ == '__main__' and len(argv) == 3:
    main(argv[1], argv[2])
