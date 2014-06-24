#!/bin/sh

#----------------------
# xml_to_crowdflower.sh
#----------------------

# Converts an xml corpus file to a Crowdflower-ready csv file

# check for proper usage
if [ $# -eq 2 ]
then
	# only write to output file if it does not already exist
	if [ ! -f $2 ]
	then
		DRIVER=com/javierllaca/hedge/driver/Main

		# if class file does not exist, create it
		if [ ! -f $DRIVER.class ]
		then
			javac -encoding utf8 $DRIVER.java
		fi

		# xml -> csv -> hedge-tagged csv
		python scripts/xml_to_csv.py $1 | java -Dfile.encoding=utf-8 $DRIVER ../database/hedges.txt > $2

	else
		# output error message and realpath of file
		echo "file already exists: $( readlink -f $2 )"
	fi
else
	echo "usage: $0 <input_file> <output_file>"
fi
