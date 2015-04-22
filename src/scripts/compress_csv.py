from csv    import reader as csv_reader
from csv    import writer as csv_writer
from sys    import argv

def number_header(header, n):
    return map(lambda s: s + "_%d" % n, header)

def duplicate_header(header, n):
    return reduce(lambda l1, l2: l1 + l2,
            [number_header(header, i) for i in range(1, n + 1)])

def csv_elems(path):
    with open(path, 'r') as csv_file:
        reader = csv_reader(csv_file, delimiter=',', quotechar='\"')
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
    writer = csv_writer(open(out_path, 'w'), delimiter=',', quotechar='\"')
    writer.writerow(new_header)
    for row in new_rows:
        writer.writerow(row)

if __name__ == '__main__':
    if len(argv) == 4:
        compress_csv(argv[1], int(argv[2]), argv[3])
    else:
        print 'Usage: python %s <in> <n> <out>' % argv[0]

