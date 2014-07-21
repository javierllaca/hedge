#!/bin/sh

HEDGE_FILE=database/hedges/relational
SLANG_FILE=database/slang

DRIVER=com/javierllaca/hedge/driver/Main

INPUT_FILE=~/speech/corpus/401

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

# Traverse file/directory -> parse -> tag -> sort -> purge
traverse $INPUT_FILE | python scripts/parse_xml.py | java -Dfile.encoding=utf-8 $DRIVER $HEDGE_FILE $SLANG_FILE | sort | uniq
