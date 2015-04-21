#!/usr/bin/python
# -*- coding: utf-8 -*-

from csv            import DictReader, DictWriter

def csv_dict(path):
    """Return a dictionary wrapping contents of csv file in path"""
    with open(path, 'r') as hedgefile:
        return DictReader(hedgefile, delimiter='\t', quotechar='\"')

#-----------------------
# compress csv
#-----------------------

def number_header(header, n):
    return map(lambda s: s + "_%d" % n, header)

def duplicate_header(header, n):
    return reduce(lambda l1, l2: l1 + l2,
            [number_header(header, i) for i in range(1, n + 1)])

def csv_elems(path):
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
    header, rows = csv_elems(in_path)
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

