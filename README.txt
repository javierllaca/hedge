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

database/	Spanish hedges and slang terms
doc/		Project documentation
src/		Source code



** ENCODING **

In order to account for non-ASCII characters in Spanish data,
the program uses UTF-8 encoding. 

Add the following flags at compilation and execution:

Compilation:
javac -encoding utf8 ...

Execution:
java -Dfile.encoding=UTF-8 ...
