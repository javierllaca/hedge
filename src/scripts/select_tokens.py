import random, sys

number = int(sys.argv[1])
log = open(sys.argv[2], 'w')

current = "" 
count = 0

term_count = 0
total = 0

ls = []

def choose(n, a):
	size = n if len(a) > n else len(a)
	for i in range(0, size):
		index = random.randrange(len(a))
		choice = a.pop(index)
		print choice

for line in sys.stdin:
	term = line[:line.index(',')].replace('\"', '')
	if term != current:
		log.write(str(count) + "\t" + current + "\n")
		choose(number, ls)

		current = term
		count = 1
		ls = [line.strip()]

		term_count += 1
	else:
		count += 1
		ls.append(line.strip())
	total += 1

log.write(str(count) + "\t" + current + "\n")
choose(number, ls)

log.write("------------------------------\n")
log.write("Total matches:\t" + str(total) + "\n")
log.write("Hedges found:\t" + str(term_count) + "\n")
