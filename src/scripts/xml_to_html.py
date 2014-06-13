import sys

if len(sys.argv) != 2:
	print "Usage: %s <input_file> <output_file>" % (sys.argv[0])
	exit()

input_file = open(sys.argv[1], 'r')
output_file = open(sys.argv[1].replace('xml/', 'html/').replace('.xml', '.html'), 'w')

output_file.write("<!DOCTYPE html>\n")
output_file.write("<html>\n")

output_file.write("<head>\n");
output_file.write("\t<meta charset=\"utf-8\">\n")
output_file.write("\t<style type=\"text/css\"> .quote { margin-left:50px; background-color:#DCDCDC } </style>\n")
output_file.write("</head>\n");

# post number counter
count = 0

for line in input_file:
	if "<doc" in line:
		output_file.write("<body>\n")
	elif "</doc" in line:
		output_file.write("\n</body>\n")
	elif "<headline" in line:
		output_file.write("\n<h1>\n")
	elif "</headline" in line:
		output_file.write("\n</h1>\n")
	elif "<post" in line:
		count += 1
		tokens = line.split('=')

		author = tokens[1].strip('=').replace('datetime', '').strip()
		date = tokens[2].replace('id', '').strip()

		output_file.write("\n<h2> %d. %s (%s) </h2>\n" % (count, author, date))
		output_file.write("<div>\n")
	elif "</post" in line:
		output_file.write("\n</div>\n")
	elif "<quote" in line:
		output_file.write("\t<div class=\"quote\"><u>Quote:</u>\n")
	elif "</quote" in line:
		output_file.write("\t</div>\n")
	elif "<?xml" in line or line[0] == '\n':
		output_file.write("\n")
	else:
		output_file.write("\t<p>" + line + "\t</p>")

output_file.write("</html>\n")
