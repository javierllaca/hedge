#!/bin/sh

HEDGE_FILE=database/hedges
SLANG_FILE=database/slang

DRIVER=com/javierllaca/hedge/Main

FORUM=401
INPUT_FILE=~/speech/corpus/forums/$FORUM

# Recursively traverse a directory by printing file contents
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

#----------------
# Text-processing
#----------------

# Recursively get text
traverse $INPUT_FILE | \

# Parse xml
python scripts/parse_xml.py | \

# Tokenize sentences (SBD)
# Normalize slang
# Tag hedges
java -Dfile.encoding=utf-8 $DRIVER $SLANG_FILE $HEDGE_FILE | \

# Sort by first column (delimited by comma)
# Remove duplicates
sort -t, -k1,1 | uniq | \

# Select some of each and log results
python scripts/select_tokens.py 2 log/new.log | \

# Append usages of tagged terms
python scripts/append_usage.py $HEDGE_FILE
