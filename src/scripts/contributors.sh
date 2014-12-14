#!/bin/sh

if [ $# -eq 1 ]
then
	FILE=~/speech/hedge/src/crowdflower/results/full/$1.csv
	if [ -e $FILE ]
	then
		cat $FILE | python contributors.py
	else
		echo $FILE 'does not exist'
	fi
else
	echo 'usage'
fi
