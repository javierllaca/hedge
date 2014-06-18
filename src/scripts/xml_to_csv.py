#--------------
# xml_to_csv.py
#--------------

# Converts corpus xml file to csv file

import sys
import re
import os

filename = sys.argv[1]
input_file = open(filename, "r")

post = False
attributes = {"author":"", "datetime":"", "id":""}

def parse_post(line):
	"""
	Parse <post> tag
	Identify author, datetime, and id attributes
	"""
	tokens = line.split('\"')
	attributes["author"] = tokens[1]
	attributes["datetime"] = tokens[3]
	attributes["id"] = tokens[5]

def clean_line(line):
	"""
	Remove <img> and <a> tags
	Escape quote characters
	Return clean line
	"""
	clean = line
	regex = "<img(.*?)/>" + "|" + "<a(.*?)</a>"	
	matches = re.finditer(regex, clean)
	for match in matches:
		clean = clean.replace(match.group(), "")
	return clean.replace("\"", "\"\"")

# Print csv header
print "author,datetime,id,file,content"

# Process lines in file
for line in input_file:
	if any(x in line for x in ["</post", "<quote"]):
		post = False
	elif post and line.strip():
		clean = clean_line(line).strip()
		if clean:
			for key in sorted(attributes.keys()):
				sys.stdout.write(attributes[key] + ",")
			sys.stdout.write(os.path.basename(filename) + ",")
			print "\"" + clean + "\""
	elif any(x in line for x in ["<post", "</quote"]):
		if "<post" in line:
			parse_post(line)
		post = True
