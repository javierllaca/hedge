from csv    import DictReader
from csv    import writer as csv_writer
from sys    import argv

def load_hits(path):
    with open(path, 'r') as csv_file:
        reader = DictReader(csv_file, delimiter=',', quotechar='\"')
        hits = {}
        for row in reader:
            hit_id = row['HITId']
            if hit_id in hits:
                hits[hit_id].append(row)
            else:
                hits[hit_id] = [row]
        return hits

def hit_to_rows(hit, n):
    rows = []
    for task in hit: # hit
        for i in range(1, n + 1):
            rows.append([
                    task['Input.hedge_%d' % i],
                    task['Input.sentence_%d' % i],
                    task['Input.gold_%d' % i],
                    task['Input.hedge_gold_%d' % i],
                    task['WorkerId'],
                    task['Answer.hedge_judgement_%d' % i]])
    return rows

def decompress_csv(in_path, n, out_path):
    """Compresses n csv rows into one"""
    writer = csv_writer(open(out_path, 'w'), delimiter=',', quotechar='\"')
    writer.writerow([
            'hedge',
            'sentence',
            'gold',
            'hedge_gold',
            'worker_id',
            'hedge_judgement'])
    hits = load_hits(in_path)
    for hit in hits:
        for row in hit_to_rows(hits[hit], n):
            writer.writerow(row)

if __name__ == '__main__':
    if len(argv) == 4:
        decompress_csv(argv[1], int(argv[2]), argv[3])
    else:
        print 'Usage: python %s <in> <n> <out>' % argv[0]
