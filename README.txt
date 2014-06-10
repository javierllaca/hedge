Spanish Hedge Detector
Javier Llaca
Speech Lab, Columbia University
---------------------------------

** File tree **

README.txt

database/
|--en/
|  |--combined_cues
|  |--lakoff.txt
|  |--multi-word_hedges.txt
|  |--p_hedge_cues.txt
|  |--r_hedge_cues.txt
|--sp/
   |--ideas.txt
   |--lakoff_en.txt
   |--lakoff_sp.txt

scripts/
|--wordcount.py
|--xml_to_csv.py
|--xml_to_html.py

src/
|--counter/
|  |--HedgeDetector.java
|--org/
|  |--apache/
|     |--commons/
|        |--lang3/
|           |--StringUtils.class
|--pride_and_prejudice.txt

** Encoding **

When running HedgeDetector:
- If input file is encoded in UTF-8, usage must be of the following form:
	java -Dfile.encoding=UTF-8 HedgeDetector <hedgeCueFile> <inputFile>
