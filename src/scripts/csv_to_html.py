import sys, csv

reader = csv.reader(sys.stdin)

rownum = 0

print '<table border=\"1\">'
for row in reader:
	if rownum == 0:
		print '\t<tr>'
		print '\t\t<th></th>'
		for column in row:
			print '\t\t<th>' + column + '</th>'
		print '\t</tr>'
	else:
		print '\t<tr>'
		print '\t\t<td>' + str(rownum) + '</td>'
		for column in row:
			print '\t\t<td valign=\"top\">' + column + '</td>'
		print '\t</tr>'
	rownum += 1

print '</table>'
