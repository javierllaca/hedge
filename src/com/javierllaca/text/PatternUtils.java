package com.javierllaca.text;

import java.util.List;
import java.util.ArrayList;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.text.Normalizer;

/**
 * Utilities for manipulating regular expression patterns
 *
 * @author Javier Llaca
 */
public class PatternUtils {

	/**
	 * Returns a copy of str with normalized non-ASCII characters
	 *
	 * @param str Input string
	 * @return ASCII-normalized String
	 */
	public static String normalizedString(String str) {
		return Normalizer.normalize(str,
				Normalizer.Form.NFD).replaceAll("[^\\p{ASCII}]", "");
	}

	/**
	 * Regex pattern containing all accented vowel characters
	 */
	public static Pattern accented() {
		return Pattern.compile("[ÁÉÍÓÚáéíóú]");
	}

	/**
	 * Determines whether str contains characters with acute accents
	 *
	 * @param str Input string
	 * @return true if character with acute accent is in str, false otherwise
	 */
	public static boolean containsAcuteAccent(String str) {
		return accented().matcher(str).find();
	}

	/**
	 * Returns a regex pattern made from a conjunction of entries in list
	 *
	 * @param list List of Strings with words to be used in pattern
	 * @return Pattern built from String entries in list
	 */
	public static Pattern conjunctionRegex(List<String> list) {
		return Pattern.compile("\\b(" + join(list, '|') + ")\\b");
	}

	/**
	 * Returns a copy of the list plus normalized versions of accented strings
	 *
	 * @param list Original list
	 */
	public static List<String> normalizedList(List<String> list) {
		List<String> copy = new ArrayList<String>();
		for (String elem : list) {
			copy.add(elem);
			if (containsAcuteAccent(elem)) {
				copy.add(normalizedString(elem));
			}
		}
		return copy;
	}

	/**
	 * Returns a string of all items in list separated by given character
	 *
	 * @param list List of Strings to be joined
	 * @param separator Separator character to use
	 * @return Joined Strings, null if empty list
	 */
	public static String join(List<String> list, Character separator) {
		String s = "";
		for (int i = 0; i < list.size() - 1; i++) {
			s += list.get(i) + separator;
		}
		return s + (list.size() > 0 ? list.get(list.size() - 1) : "");
	}
}
