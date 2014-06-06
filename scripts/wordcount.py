import sys

file_object = open(sys.argv[1], 'r')

words = dict()

for line in file_object:
	tokens = line.split()
	for tok in tokens:
		if tok not in words:
			words[tok] = 1
		else:
			words[tok] += 1

for word in words:
	#if words[word] > 5:
	print "%-15s%d" % (word, words[word])
