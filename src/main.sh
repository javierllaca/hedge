#!/bin/sh

SLANG=database/slang
HEDGE=database/hedges

DRIVER=com/javierllaca/hedge/Main

FORUM=387
INPUT=~/speech/corpus/forums/$FORUM
LOG=$FORUM.log

TOKENS=10

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
echo "hedge,sentence,usage1,usage2" > csv/$FORUM.csv

# Output content of directory
traverse $INPUT | \

# Parse XML content
python scripts/parse_xml.py | \

# Main Java engine: Tokenize sentences, Normalize slang, Tag hedges
java -Dfile.encoding=utf-8 $DRIVER $SLANG $HEDGE | \

# Sort by hedge (first column)
sort -t, -k1,1 | \

# Remove duplicates
uniq | \

# Select tokens and log results
python scripts/select_tokens.py $TOKENS log/$LOG | \

# Append usages of tagged terms
python scripts/append_usage.py $HEDGE | \

# Randomize rows for crowdsourcing task
shuf >> csv/$FORUM.csv
