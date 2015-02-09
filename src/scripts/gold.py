from csv import DictReader, DictWriter
from sys import argv, stdin, stdout

def join(ls, delim):
	return reduce(lambda a,b: a + delim + b, ls)

def order(ordering, mapping):
	ordered = []
	for key in ordering:
		ordered.append(mapping[key])
	return ordered

def parse_response(c):
	if len(c) == 0 or c[0] != 'y':
		return 'false'
	return 'true'

def main(in_path, out_path):
	reader = DictReader(open(in_path, 'r'))
	writer = DictWriter(open(out_path, 'wb'), 
			fieldnames=reader.fieldnames + ['gold', 'hedge_gold'])

	writer.writeheader()

	rows, gold_rows = 0, 0

	for row in reader:
		gold, response = 'false', ''

		print '-' * 20
		print '[', gold_rows, ']\n'
		print rows + 1, row['sentence'], '\n'
		print 'Gold?',

		if raw_input() == 'y':
			gold = 'true'
			gold_rows += 1
			print 'Hedge?',
			response = parse_response(raw_input())

		row['gold'] = gold
		row['hedge_gold'] = response

		writer.writerow(row)
		rows += 1

		print

if __name__ == '__main__' and len(argv) == 3:
	main(argv[1], argv[2])
