Spanish Hedge Detector

Author: Javier Llaca
Speech Lab - Department of Computer Science, Columbia University
----------------------------------------------------------------

** OVERVIEW **

This program detects and tags potential hedges in Spanish text.

More specifically, the program goes through a Spanish corpus,
extracts usable text, analyzes it, and produces a csv file for 
use in a crowd-sourcing task.

The csv file contains random and evenly-distributed instances 
of possible hedges in the corpus.



** DEPENDENCIES **

Java Libraries:
- Apache OpenNLP (https://opennlp.apache.org)



** DIRECTORY STRUCTURE **

doc/		Project documentation
src/		Source code (includes hedge and slang term database)



** ENCODING **

In order to account for non-ASCII characters in Spanish data,
UTF-8 is used for text encoding. 

The following flags are added at compilation and execution:
javac -encoding utf8 ...	(compilation)
java -Dfile.encoding=UTF-8 ...	(execution)
