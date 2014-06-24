package com.javierllaca.hedge.tag;

import com.javierllaca.io.Input;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

/**
 * Tags lines of text according to a text database
 * @author Javier Llaca
 */
public class Tagger
{
	/**
	 * String used in tag
	 */
	private String tag;

	/**
	 * Pattern to be queried
	 */
	private Pattern pattern;

	/**
	 * Initializes tag and creates a Pattern from terms in file
	 * @param filename Path to term file
	 */
	public Tagger(String filename, String tag)
	{
		this.tag = tag;
		List<String> terms = termListFromFile(filename);
		this.pattern = PatternUtils.createRegexFromList(terms);
	}

	/** 
	 * Returns a list containing terms in file
	 * @param filename Path to term file
	 * @return List with terms in file
	 */
	public List<String> termListFromFile(String filename)
	{
		Input in = new Input(filename);
		List<String> terms = new ArrayList<String>();
		while (in.hasNextLine()) {
			String line = in.readLine().trim();
			if (!line.isEmpty()) {
				terms.add(line);
				if (PatternUtils.containsAcuteAccent(line))
					terms.add(PatternUtils.normalizeEncoding(line));
			}
		}
		in.close();
		return terms;
	}

	/**
	 * Returns an ArrayList containing all versions of tagged line
	 * @param line Input line
	 */
	public ArrayList<String> tagLine(String line)
	{
		ArrayList<String> tags = new ArrayList<String>();
		Matcher matcher = this.pattern.matcher(line);

		while (matcher.find()) {
			StringBuilder tag = new StringBuilder(line);
			tags.add(new String(tag.insert(matcher.end(), "</" + this.tag + ">").insert(
						matcher.start(), "<" + this.tag + ">")));
		}

		return tags;
	}
}
