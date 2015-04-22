from csv            import DictReader
from csv            import writer as csv_writer
from unicodedata    import normalize as norm
from sys            import argv

def normalize(s):
    """Normalize utf8 characters to their ascii equivalents"""
    return norm('NFD', s.decode('utf8')).encode('ascii', 'ignore')

def load_units(path):
    with open(path, 'r') as csv_file:
        reader = DictReader(csv_file, delimiter=',', quotechar='\"')
        units = {}
        for row in reader:
            unit = (row['hedge'],
                    row['sentence'])
            val = (row['worker_id'],
                    row['hedge_judgement'])
            if unit in units:
                units[unit].append(val)
            else:
                units[unit] = [val]
        return units

def unit_judgements(unit):
    judgements = {
            'TRUE'  : 0,
            'FALSE' : 0,
            ''      : 0} # no judgement
    for worker, judgement in unit:
        judgements[judgement] += 1
    return judgements

def fuzzy(judgements):
    yes, no = judgements['TRUE'], judgements['FALSE']
    return abs(yes - no) <= 1

def change_tag(line):
    return line.replace('<strong>', '[').replace('</strong>', ']')

def load_hedge_types(path):
    with open(path, 'r') as csv_file:
        reader = DictReader(csv_file, delimiter=',', quotechar='\"')
        hedges = {}
        for row in reader:
            hedges[normalize(row['hedge']).strip()] = row['hedge_type']
        return hedges

def print_unit(unit, judgements, hedge_types):
    hedge, sent = unit
    yes, no = judgements['TRUE'], judgements['FALSE']
    if yes > no:
        print '%s\t%s\t%s' % (change_tag(sent), hedge, hedge_types[hedge])
    else:
        print '%s\t%s\tNH' % (change_tag(sent), hedge)

def list_to_csv(ls, path, hedge_path):
    hedge_types = load_hedge_types(hedge_path)
    writer = csv_writer(open(path, 'w'), delimiter='\t', quotechar='\"')
    writer.writerow([
            'segment',
            'proposition',
            'belief_type'])
    for unit, judgements in ls:
        hedge, sent = unit
        yes, no = judgements['TRUE'], judgements['FALSE']
        if yes > no:
            writer.writerow([change_tag(sent), hedge, hedge_types[hedge]])
        else:
            writer.writerow([change_tag(sent), hedge, 'NH'])

def annotate(in_path, out_path, hedge_path):
    units = load_units(in_path)
    good, bad = [], []
    for unit in units:
        judgements = unit_judgements(units[unit])
        if not fuzzy(judgements):
            good.append((unit, judgements))
        else:
            bad.append((unit, judgements))
    list_to_csv(good, out_path, hedge_path)

if __name__ == '__main__':
    if len(argv) == 4:
        annotate(argv[1], argv[2], argv[3])
    else:
        print 'Usage: python %s <in> <out> <hedges>' % argv[0]

