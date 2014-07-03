Spanish Hedge Detector

Author: Javier Llaca
Speech Lab - Department of Computer Science, Columbia University
----------------------------------------------------------------

** OVERVIEW **

This program detects and tags potential hedges in Spanish text.



** DEPENDENCIES **

Java Libraries:
- Apache OpenNLP
- Apache Commons Lang



** DIRECTORY STRUCTURE **

crowdflower/	Documents used in crowd-sourcing task
database/	Data used in program
src/		Source code
test_files/	Miscellanous files for testing program



** ENCODING **

In order to account for non-ASCII characters in Spanish data,
the program uses UTF-8 encoding. 

Add the following flags for compilation and execution:

Compilation:
javac -encoding utf8 ...

Execution:
java -Dfile.encoding=UTF-8 ...
