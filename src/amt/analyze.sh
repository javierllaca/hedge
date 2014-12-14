#!/bin/sh

# Analyze results csv files from CrowdFlower

if [ $# -eq 1 ]
then
	BASENAME=${1##*/}
	OUTPUT=${BASENAME%.*}.txt

	ANNOTATION_FILE=analysis/annotation/$OUTPUT
	STATS_FILE=analysis/stats/$OUTPUT

	echo $ANNOTATION_FILE $STATS_FILE

	if [ ! -e $ANNOTATION_FILE ] && [ ! -e $STATS_FILE ]
	then
		CONFIDENCE_THRESHOLD=0.8
		HEDGES=~/speech/hedge/src/database/hedges
		SCRIPTS=~/speech/hedge/src/scripts

		# Print header to output file
		echo "segment\tproposition\tbelief_type" > $ANNOTATION_FILE

		# Print input file
		cat $1 | \

		# Get data with judgement confidence above threshold
		python $SCRIPTS/parse_results.py $CONFIDENCE_THRESHOLD | \

		# Tag relational hedges
		python $SCRIPTS/classify.py $HEDGES/relational HREL | \

		# Tag propositional hedges and append results to output file
		python $SCRIPTS/classify.py $HEDGES/propositional HPROP >> $ANNOTATION_FILE

		# Print stats to console
		cat $1 | python $SCRIPTS/results_stats.py > $STATS_FILE
	else
		echo "Output files already exist"
	fi
else
	echo "Usage: $0 <input_file>"
fi
