#----------
# purge.csv
#----------

# Prints csv heading and only rows with <strong> tags to stdout

import sys

print sys.stdin.readline(),

for line in sys.stdin:
	if "<strong>" in line:
		print line,
