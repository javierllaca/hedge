#!/bin/sh

# Analyze results csv files from CrowdFlower

if [ $# -eq 1 ]
then
	basename=${1##*/}
	output_file=annotation/${basename%.*}.txt

	# Print header to output file
	echo "segment\tproposition\tbelief_type" > $output_file

	# Print input file
	cat $1 | \

	# Get gold data
	python scripts/parse_results.py | \

	# Tag relational hedges
	python scripts/classify.py database/hedges/relational HREL | \

	# Tag propositional hedges and append results to output file
	python scripts/classify.py database/hedges/propositional HPROP >> $output_file

	# Print stats to console
	cat $1 | python scripts/results_stats.py
	echo "\n(Annotations in $output_file)"
else
	echo "Usage: $0 <file>"
fi
