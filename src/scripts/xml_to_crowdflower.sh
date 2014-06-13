#!/bin/sh

if [ $# -eq 2 ]
then
	# only write to target file if it does not already exist
	# mainly for security purposes
	if [ ! -f $2 ]
	then
		if [ ! -f detector/HedgeDetector.class ]
		then
			javac -encoding utf8 detector/HedgeDetector.java
		fi

		python scripts/xml_to_csv.py $1 | java -Dfile.encoding=utf-8 detector/HedgeDetector ../cues/draft.txt | python scripts/purge_csv.py > $2

	else
		echo "output file already exists"
	fi
else
	echo "usage: $0 <input_file> <output_file>"
fi
