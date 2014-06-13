Spanish Hedge Detector
Javier Llaca
Speech Lab, Columbia University
---------------------------------

** File tree **

README.txt

crowdflower/
|--instructions

cues/
|--draft.txt

src/
|--detector/
|  |--HedgeDetector.java
|--org/
|  |--apache/
|     |--commons/
|        |--lang3/
|           |--StringUtils.class
|--scripts/
   |--purge_csv.py
   |--wordcount.py
   |--xml_to_crowdflower.sh
   |--xml_to_csv.py
   |--xml_to_html.py

test_files/
|--epn.xml
|--borges.txt


** Encoding **

Since the program is designed for processing Spanish data, everything must
be encoded in UTF-8. When compiling and running the program, add the following
flags:

Compilation:
javac -encoding utf8 detector/HedgeDetector.java

Runtime:
java -Dfile.encoding=UTF-8 detector.HedgeDetector <hedgeCueFile> <inputFile>
