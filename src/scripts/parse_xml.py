#--------------
# parse_xml.py
#--------------

# Prints text body of corpus xml files

import fileinput
import re

post = False

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
	return clean #.replace("\"", "\"\"")

# Process lines in file
for line in fileinput.input():
	if any(x in line for x in ["</post", "<quote"]):
		post = False
	elif post and line.strip():
		clean = clean_line(line).strip()
		if clean:
			print clean
	elif any(x in line for x in ["<post", "</quote"]):
		post = True
