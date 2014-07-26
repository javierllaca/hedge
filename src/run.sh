#!/bin/sh

SLANG_FILE=database/slang
HEDGE_FILE=database/hedges

DRIVER=com/javierllaca/hedge/Main

INPUT_FILE=~/speech/corpus/forums/401
LOG_FILE=401.log

# Recursively output content of files in directory
traverse () {
	if [ -d $1 ]
	then
		for f in $1/*
		do
			traverse $f
		done
	else
		cat $1 
	fi
}

# Compile java code
javac -encoding utf8 $DRIVER.java

# Print csv header
echo "hedge,sentence,usage1,usage2"

# Output content of directory
traverse $INPUT_FILE | \

# Parse XML content
python scripts/parse_xml.py | \

'''
Main Java engine:
	- Tokenize sentences
	- Normalize slang
	- Tag hedges
'''
java -Dfile.encoding=utf-8 $DRIVER $SLANG_FILE $HEDGE_FILE | \

# Sort by hedge (first column)
sort -t, -k1,1 | 

# Remove duplicates
uniq | \

# Select tokens and log results
python scripts/select_tokens.py 2 log/$LOG_FILE | \

# Append usages of tagged terms
python scripts/append_usage.py $HEDGE_FILE | \

# Randomize rows for crowdsourcing task
shuf
