#!/bin/sh

if [ $# -eq 1 ]
then
	FILE=~/speech/hedge/src/crowdflower/results/aggregate/$1.csv
	if [ -e $FILE ]
	then
		cat $FILE | python hedges.py
	else
		echo $FILE 'does not exist'
	fi
else
	echo 'usage'
fi
