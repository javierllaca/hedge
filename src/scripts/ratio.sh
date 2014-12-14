#!/bin/sh

if [ $# -eq 1 ]
then
	FILE=~/speech/hedge/src/crowdflower/results/aggregate/$1.csv
	echo $FILE
	if [ -e $FILE ]
	then
		cat $FILE | python ratio.py
	else
		echo 'file does not exist'
	fi
else
	echo 'usage'
fi
