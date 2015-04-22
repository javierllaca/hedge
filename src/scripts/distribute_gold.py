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

