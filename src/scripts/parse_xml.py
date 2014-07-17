#--------------
# parse_xml.py
#--------------

# Prints text body of corpus xml files

import fileinput, re

post = False

def clean_line(line):
	"""
	Return line without <img> and <a> tags
	"""
	clean = line
	regex = "<img(.*?)/>" + "|" + "<a(.*?)</a>"	
	matches = re.finditer(regex, clean)
	for match in matches:
		clean = clean.replace(match.group(), "")
	return clean

# Iterate through lines in input
for line in fileinput.input():
	if any(x in line for x in ["</post", "<quote"]):
		post = False
	elif post and line.strip():
		clean = clean_line(line).strip()
		if clean:
			print clean
	elif any(x in line for x in ["<post", "</quote"]):
		post = True
