#!/bin/sh

#-----------
# convert.sh
#-----------

# Processes all xml files in a corpus directory
# Converts them to CrowdFlower-ready csv files

FILES=$1/xml/*.xml
OUTDIR=$1/../csv

if [ $# -eq 1 ]
then
	if [ ! -d $OUTDIR ]
	then
		mkdir $OUTDIR	
	fi

	# process every file with xml_to_crowdflower script
	for i in $FILES
	do
		basename=${i##*/}
		filename=${basename%.xml}.csv
		target=$OUTDIR/$filename
		scripts/xml_to_crowdflower.sh $i $target
	done
else
	echo "Usage: $0 <corpusDirectory>"
fi
