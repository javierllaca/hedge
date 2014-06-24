Spanish Hedge Detector

Javier Llaca
Speech Lab, Columbia University
-------------------------------

** OVERVIEW **

This program detects and tags potential hedges in Spanish text.




** DIRECTORY STRUCTURE **

crowdflower/	Documents used in crowd-sourcing task
database/	Data used in program
src/		Source code
test_files/	Miscellanous files for testing program

README.txt	This file




** ENCODING **

In order to account for non-ASCII characters in Spanish data,
the program uses UTF-8 encoding. 

Add the following flags for compilation and execution:

Compilation:
javac  detector/HedgeDetector.java

Execution:
java -Dfile.encoding=UTF-8 detector.HedgeDetector <hedgeFile> 
