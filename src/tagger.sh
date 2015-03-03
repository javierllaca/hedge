#!/bin/sh

DRIVER=com/javierllaca/hedge/Main

CLASSPATH=~/java
DEPENDENCIES="$CLASSPATH/*":.

SLANG=database/slang.csv
HEDGE=database/hedges.csv

FORUM=$1
TOKENS=$2

INPUT=~/speech/corpus/forums/$FORUM
OUTPUT=amt/input/$FORUM.csv
LOG=$FORUM.log

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

if [ $# -eq 2 ]
then
        # Compile all relevant java code
        javac -encoding utf8 -cp $DEPENDENCIES $DRIVER.java

        # Print csv header
        echo "hedge,sentence,usage_a,usage_b" > $OUTPUT

        # Output content of directory
        traverse $INPUT | \

        # Parse XML content
        python scripts/parse_xml.py | \

        # Main Java engine:
        # - Tokenize sentences
        # - Normalize slang
        # - Tag hedges
        java -Dfile.encoding=utf-8 -cp $DEPENDENCIES $DRIVER $SLANG $HEDGE | \

        # Sort alphabetically by hedge (first column)
        sort -t, -k1,1 | \

                # Remove duplicates
        uniq | \

        # Select tokens and log results
        python scripts/select_tokens.py $TOKENS log/$LOG | \

        # Append usages of tagged terms
        python scripts/append_usage.py $HEDGE | \

        # Randomize rows for crowdsourcing task
        shuf >> $OUTPUT
else
        echo 'Usage:' $0 '<forum> <# tokens>'
fi
