package com.javierllaca.text;

import com.javierllaca.io.Input;
import com.javierllaca.collect.Pair;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

/**
 * Tags lines of text according to a text database
 *
 * @author Javier Llaca
 */
public class Tagger {

  /**
   * Label used in tags
   */
  private String label;

  /**
   * Regex pattern to be queried
   */
  private Pattern pattern;

  /**
   * Initializes tag and creates a Pattern from terms in file
   *
   * @param label Label used by tagger
   * @param pattern Regex pattern used for matching
   *
   */
  public Tagger(String label, Pattern pattern) {
    this.label = label;
    this.pattern = pattern;
  }

  /**
   * Returns an ArrayList containing all versions of tagged line
   *
   * @param line Input line
   * @return List of versions of tagged line if at least one match is found;
   * empty list otherwise
   */
  public ArrayList<Pair<String,String>> tagLine(String line) {
    ArrayList<Pair<String,String>> tags = new ArrayList<Pair<String,String>>();
    Matcher matcher = this.pattern.matcher(line);

    while (matcher.find()) {
      String match = PatternUtils.normalizedString(matcher.group()).toLowerCase();
      String tagged = tag(line, this.label, match, matcher.start(), matcher.end());
      tags.add(new Pair<String,String>(match, tagged));
    }

    return tags;
  }

  /**
   * Returns line with all matches tagged
   *
   * @param line Input line
   * @param query Word to be tagged
   * @param label Label to be used in tag
   * @return Tagged line if query is found; unmodified line otherwise
   */
  public static String tagLine(String line, String query, String label) {
    String regex = PatternUtils.normalizedString(query) + "|" + 
      PatternUtils.normalizedString(capitalize(query));

    Pattern pattern = Pattern.compile(regex);
    Matcher matcher = pattern.matcher(PatternUtils.normalizedString(line));

    while (matcher.find()) {
      line = tag(line, label, matcher.group(), matcher.start(), matcher.end());
      matcher = pattern.matcher(PatternUtils.normalizedString(line));
    }

    return line;
  }

  /**
   * Returns line with specified match tagged at specified indeces
   *
   * @param line Line to be tagged
   * @param label Label to be used in tag
   * @param match String to be tagged
   * @param start Start index of match
   * @param end End index of match
   * @return Tagged line
   */
  public static String tag(String line, String label, String match, int start, 
      int end) {
    StringBuilder result = new StringBuilder(line.substring(0, start));
    result.append("<" + label + ">" + match + "</" + label + ">");
    return result.append(line.substring(end)).toString();
  }

  /**
   * Returns the capitalized string
   *
   * @param line Input String
   * @return String with upper case first character
   */
  private static String capitalize(String line) {
    return Character.toUpperCase(line.charAt(0)) + line.substring(1);
  }
}
