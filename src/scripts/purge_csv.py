import sys

print sys.stdin.readline(),

for line in sys.stdin:
	if "<strong>" in line:
		print line,
