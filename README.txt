Spanish Hedge Detector

Author: Javier Llaca
Speech Lab - Department of Computer Science, Columbia University
----------------------------------------------------------------

** OVERVIEW **

This program detects and tags potential hedges in Spanish text.



** DEPENDENCIES **

Java Libraries:
- Apache OpenNLP (https://opennlp.apache.org)



** DIRECTORY STRUCTURE **

database/	Spanish hedges and slang term mappings
doc/		Project documentation
src/		Source code



** ENCODING **

In order to account for non-ASCII characters in Spanish data,
UTF-8 is used for text encoding. 

Add the following flags at compilation and execution:

Compilation:
javac -encoding utf8 ...

Execution:
java -Dfile.encoding=UTF-8 ...
