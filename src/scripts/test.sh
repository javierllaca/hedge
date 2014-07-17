#!/bin/sh

DRIVER=com/javierllaca/hedge/driver/Main
HEDGE_FILE=../database/hedges/relational
INPUT_FILE=~/speech/corpus/399-3/xml

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
traverse $INPUT_FILE | python scripts/parse_xml.py | java -Dfile.encoding=utf-8 $DRIVER $HEDGE_FILE | sort | uniq
