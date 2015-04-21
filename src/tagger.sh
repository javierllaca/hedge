#!/bin/sh

FORUM=$1
TOKENS=$2

DRIVER=com/javierllaca/hedge/Main
CLASSPATH=jar/*:.

PROCESS=py/pre

SLANG=db/slang.csv
HEDGE=db/hedges.csv

INPUT=corpus/$FORUM
OUTPUT=amt/pre/$FORUM.csv

LOG=$FORUM.log

# Recursively output content of files in directory
traverse () {
        if [ -d $1 ]; then
                for f in $1/*; do
                        traverse $f
                done
        else
                cat $1 
        fi
}

if [ $# -eq 2 ]; then
        # Compile all relevant java code
        javac -encoding utf8 -cp $CLASSPATH $DRIVER.java

        # Print csv header
        echo "hedge,sentence,usage_a,usage_b,gold,hedge_gold" > $OUTPUT

        # Output content of directory
        traverse $INPUT | \

        # Parse XML content
        python $PROCESS/parse_xml.py | \

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
        python $PROCESS/select_tokens.py $TOKENS log/$LOG | \

        # Append usages of tagged terms
        python $PROCESS/append_usage.py $HEDGE | \

        # Randomize rows for crowdsourcing task
        shuf >> $OUTPUT
else
        echo 'Usage:' $0 '<forum> <# tokens>'
fi
