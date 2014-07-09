package com.javierllaca.hedge.tag;

import com.javierllaca.io.Input;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

/**
 * Tags lines of text according to a text database
 * @author Javier Llaca
 */
public class Tagger {
	/**
	 * String used in tag
	 */
	private String tag;

	/**
	 * Pattern to be queried
	 */
	private Pattern pattern;

	/**
	 * Map of a term to its definitions
	 */
	private HashMap<String, ArrayList<String>> map;

	/**
	 * Initializes tag and creates a Pattern from terms in file
	 * @param filename Path to term file
	 */
	public Tagger(String filename, String tag) {
		this.tag = tag;
		this.map = new HashMap<String, ArrayList<String>>();
		this.pattern = PatternUtils.createRegexFromList(termListFromFile(filename));
	}

	/** 
	 * Returns a list containing terms in file
	 * @param filename Path to term file
	 * @return List with terms in file
	 */
	public List<String> termListFromFile(String filename) {
		Input in = new Input(filename);
		while (in.hasNextLine()) {
			String line = in.readLine().trim();

			if (!line.isEmpty()) {

				String[] tokens = line.split("\t");
				String term = tokens[0];

				ArrayList<String> definitions = new ArrayList<String>();

				for (int i = 1; i < tokens.length; i++) {
					definitions.add(tokens[i]);
				}

				map.put(term, definitions);

				if (PatternUtils.containsAcuteAccent(line)) {
					String normalized = PatternUtils.normalizeEncoding(term);
					map.put(normalized, definitions);
				}
			}
		}
		in.close();
		return new ArrayList<String>(map.keySet());
	}

	/**
	 * Returns an ArrayList containing all versions of tagged line
	 * @param line Input line
	 */
	public ArrayList<String> tagLine(String line) {
		ArrayList<String> tags = new ArrayList<String>();
		Matcher matcher = this.pattern.matcher(line);

		while (matcher.find()) {
			String term = matcher.group();

			StringBuilder temp = (new StringBuilder(line));
			temp.insert(matcher.end(), "</" + this.tag + ">");
			temp.insert(matcher.start(), "<" + this.tag + ">");

			String tag = "\"" + temp.toString().replace("\"", "\"\"") + "\",\"" + term + "\"";
			for (String def : map.get(term)) {
				tag += ",\"" + def + "\"";
			}
			tags.add(tag);
		}

		return tags;
	}
}
