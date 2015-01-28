# Hedging in Spanish

Source code and documentation for research project on hedges -

Author: Javier Llaca
Speech Lab - Department of Computer Science, Columbia University

## Overview

This program detects and tags potential hedges in Spanish text.

More specifically, the program goes through a Spanish corpus,
extracts usable text, analyzes it, and produces a csv file for 
use in a crowd-sourcing task.

The csv file contains random and evenly-distributed instances 
of possible hedges in the corpus.

## Dependencies

Java Libraries:
- Apache OpenNLP (https://opennlp.apache.org)

## Directory Structure

doc/		Project documentation
src/		Source code (includes hedge and slang term database)

## ENCODING

In order to account for non-ASCII characters in Spanish data,
UTF-8 is used for text encoding. 

The following flags are added at compilation and execution, respectively:

```
javac -encoding utf8 ...
java -Dfile.encoding=UTF-8 ...
```
