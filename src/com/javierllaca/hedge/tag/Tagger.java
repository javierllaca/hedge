package com.javierllaca.hedge.tag;

import com.javierllaca.io.Input;

import java.io.File;
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

		loadTerms(filename);
		List<String> hedges = new ArrayList<String>(map.keySet());

		this.pattern = PatternUtils.createRegexFromList(hedges);
	}

	/** 
	 * Loads terms and definitions to from file into a HashMap
	 * If filename points to a directory, files inside are accessed recursively
	 * @param filename Path to term file
	 */
	public void loadTerms(String filename) {
		File file = new File(filename);
		if (file.isDirectory()) {
			File[] files = file.listFiles();
			for (File f : files) {
				loadTerms(f.toString());
			}
		}
		else {
			Input in = new Input(filename);
			while (in.hasNextLine()) {
				String line = in.readLine().trim();

				if (!line.isEmpty()) {
					String[] tokens = line.split("\\t+");
					String term = tokens[0];

					ArrayList<String> definitions = new ArrayList<String>();

					for (int i = 1; i < tokens.length; i++) {
						definitions.add(tagLine(tokens[i], term, this.tag));
					}

					map.put(term, definitions);
					map.put(capitalize(term), definitions);

					if (PatternUtils.containsAcuteAccent(line)) {
						String normalized = PatternUtils.normalizeEncoding(term);
						map.put(normalized, definitions);
						map.put(capitalize(normalized), definitions);
					}
				}
			}
			in.close();
		}
	}

	/**
	 * Returns an ArrayList containing all versions of tagged line
	 * @param line Input line
	 * @return List of versions of tagged line if at least one match is found; empty list otherwise
	 */
	public ArrayList<String> tagLine(String line) {
		ArrayList<String> tags = new ArrayList<String>();
		Matcher matcher = this.pattern.matcher(line);

		while (matcher.find()) {
			String term = matcher.group().toLowerCase();

			StringBuilder temp = (new StringBuilder(line));
			temp.insert(matcher.end(), "</" + this.tag + ">");
			temp.insert(matcher.start(), "<" + this.tag + ">");

			String tag = "\"" + term + "\",\"" + temp.toString().replace("\"", "\"\"") + "\"";
			for (String def : map.get(term)) {
				tag += ",\"" + def + "\"";
			}
			tags.add(tag);
		}

		return tags;
	}

	/**
	 * Returns the tagged line
	 * @param line Input line
	 * @param query Word to be tagged
	 * @param tag Tag to be used
	 * @return Tagged line if query is found; unmodified line otherwise
	 */
	public static String tagLine(String line, String query, String tag) {
		String regex = PatternUtils.normalizeEncoding(query) + "|" + 
			PatternUtils.normalizeEncoding(capitalize(query));
		Matcher matcher = Pattern.compile(regex).matcher(PatternUtils.normalizeEncoding(line));

		if (matcher.find()) {
			StringBuilder temp = (new StringBuilder(line));
			temp.insert(matcher.end(), "</" + tag + ">");
			temp.insert(matcher.start(), "<" + tag + ">");
			return new String(temp);
		}
		return line;
	}
	
	/**
	 * Returns the capitalized string
	 * @param line Input String
	 * @return String with upper case first character
	 */
	private static String capitalize(String line) {
		  return Character.toUpperCase(line.charAt(0)) + line.substring(1);
	}
}
