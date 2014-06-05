import sys

if len(sys.argv) != 2:
	print "Usage: %s <input_file> <output_file>" % (sys.argv[0])
	exit()

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[1].replace('.xml', '') + '.html', 'w')

output_file.write("<!DOCTYPE html>")
output_file.write("<html>")
output_file.write("<meta charset=\"utf-8\">")

# post number counter
count = 0

for line in input_file:
	if "<doc" in line:
		output_file.write("<body>\n")
	elif "</doc" in line:
		output_file.write("</body>\n")
	elif "<headline" in line:
		output_file.write("\n<h1>\nTema: \n")
	elif "</headline" in line:
		output_file.write("</h1>\n")
	elif "<post" in line:
		count += 1
		tokens = line.split('=')

		author = tokens[1].strip('=').replace('datetime', '').strip()
		date = tokens[2].replace('id', '').strip()

		output_file.write("\n<h2> %d. %s (%s) </h2>\n" % (count, author, date))
		output_file.write("<p>\n")
	elif "</post" in line:
		output_file.write("</p>\n")
	else:
		output_file.write(line)

output_file.write("</html>\n")
