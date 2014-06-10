import sys
import re

input_file = open(sys.argv[1], "r")

post = False
attributes = {"author":"", "datetime":"", "id":""}

def parse_post(line):
	for key in attributes:
		attributes[key] = line[(line.index(key)):].split('\"')[1]

# remove <img> and <a> tags
# escape quote characters
def clean_line(line):
	clean = line
	regex = "<img(.*?)/>" + "|" + "<a(.*?)</a>"	
	matches = re.finditer(regex, clean)
	for match in matches:
		clean = clean.replace(match.group(), "")
	return clean.replace("\"", "\"\"")

print "author,datetime,id,content"

for line in input_file:
	if any(x in line for x in ["</post", "<quote"]):
		post = False
	elif post and line.strip():
		for key in sorted(attributes.keys()):
			sys.stdout.write(attributes[key] + ",")
		print "\"" + clean_line(line.strip()) + "\""
	if any(x in line for x in ["<post", "</quote"]):
		if "<post" in line:
			parse_post(line)
		post = True
