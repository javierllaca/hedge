package com.javierllaca.text;

import com.javierllaca.csv.MyCSV;
import com.javierllaca.io.Input;
import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

/**
 * Normalizes text according to a database of term mappings
 *
 * @author Javier Llaca
 */
public class TermNormalizer {

	/**
	 * Map of strings of one type to their equivalent
	 */
	private HashMap<String,String> map;

	/**
	 * Conjunction regex 
	 */
	private Pattern pattern;

	/**
	 * Initializes term map and creates a Pattern from terms in file
	 *
	 * @param filename Path to term file
	 * @param col1 Name of column 1 header
	 * @param col2 Name of column 2 header
	 */
	public TermNormalizer(String filename, String col1, String col2) {
		this.map = csvMap(filename, col1, col2);
		this.pattern = PatternUtils.conjunctionRegex(
				new ArrayList<String>(this.map.keySet()));
	}

	/**
	 * Returns a mapping from strings to strings based on the first two
	 * columns of a csv file.
	 *
	 * @param filename Path to term file
	 * @param col1 Column 1 header name
	 * @param col2 Column 2 header name
	 * @return List with terms
	 */
	public HashMap<String,String> csvMap(String filename, String col1, String col2) {
		HashMap<String,String> map = new HashMap<String,String>();

		MyCSV csv = new MyCSV(filename);
		List<String> l1 = csv.colValues(col1);
		List<String> l2 = csv.colValues(col2);

		for (int i = 0; i < l1.size(); i++) {
			map.put(l1.get(i), l2.get(i));
		}

		return map;
	}

	/**
	 * Returns a copy of str with elements with and without encoding normalization
	 * 
	 * @param line Input line
	 * @return Term-normalized String
	 */
	public String normalizeLine(String line) {
		Matcher matcher = pattern.matcher(line);
		StringBuffer sb = new StringBuffer();
		while (matcher.find()) {
			matcher.appendReplacement(sb, map.get(matcher.group()));
		}
		matcher.appendTail(sb);
		return new String(sb);
	}
}
