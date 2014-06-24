package detector;

import java.io.File;
import java.io.FileNotFoundException;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.Scanner;

import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.text.Normalizer;

import org.apache.commons.lang3.StringUtils;

/**
 * Detects and tags potential hedge cues in stdin
 * @author Javier Llaca
 */
public class HedgeDetector
{
	/**
	 * Contains hedge cues
	 */
	public static ArrayList<String> cues;

	/**
	 * Contains slang terms
	 */
	public static ArrayList<String> slang;

	/**
	 * Contains slangs terms and their equivalences
	 */
	public static HashMap<String, String> slangMap;

	public static HashMap<String, ArrayList<String>> hedges;

	/**
	 * Default constructor
	 */
	public HedgeDetector() {}

	/** 
	 * Loads hedge cues in file into an ArrayList object
	 * @param filename Path to hedge cue file
	 * @return Regular expression pattern built from all hedge cues
	 */
	public static Pattern loadCues(String filename)
	{
		try {
			File cueFile = new File(filename);
			Scanner db = new Scanner(cueFile);

			cues = new ArrayList<String>();
			while (db.hasNextLine()) {
				String line = db.nextLine().trim();
				if (!line.isEmpty()) {
					cues.add(line);
					if (containsAcuteAccent(line))
						cues.add(normalized(line));
				}
			}

			db.close();

			return regex(cues);

		} catch (FileNotFoundException e) {};
		return Pattern.compile("");
	}

	/**
	 * Loads slang terms and equivalences into an ArrayList object
	 * @param filename Path to slang term file
	 * @return Regular expression pattern built from all slang terms
	 */
	public static Pattern loadSlang(String filename)
	{
		try {
			slangMap = new HashMap<String, String>();
			File file = new File(filename);
			Scanner in = new Scanner(file);

			while (in.hasNextLine()) {
				String tok[] = in.nextLine().split("\t");
				slangMap.put(tok[0], tok[1]);
			}

			slang = new ArrayList<String>(slangMap.keySet());
			
			in.close();

			return regex(slang);

		} catch(FileNotFoundException e) {
			System.out.println(e);
		};
		return Pattern.compile("");
	}

	/**
	 * Returns a copy of str with slang replaced by equivalent full words
	 * @param str Input string
	 * @param slang Pattern with slang terms to be queried
	 * @return Slang-normalized String
	 */
	public static String nonSlang(String str, Pattern slang)
	{
		Matcher matcher = slang.matcher(str);
		StringBuffer sb = new StringBuffer();

		while (matcher.find())
			matcher.appendReplacement(sb, slangMap.get(matcher.group()));

		matcher.appendTail(sb);

		return new String(sb);
	}

	/**
	 * Returns copy of str with normalized non-ASCII characters
	 * @param str Input string
	 * @return ASCII-normalized String
	 */
	public static String normalized(String str)
	{
		return Normalizer.normalize(str, Normalizer.Form.NFD).replaceAll("[^\\p{ASCII}]", "");
	}

	/**
	 * Determines whether str contains characters with acute accent
	 * @param str Input string
	 * @return true if character with acute accent is in str, false otherwise
	 */
	public static boolean containsAcuteAccent(String str)
	{
		Pattern pattern = Pattern.compile("[ÁÉÍÓÚáéíóú]");
		Matcher matcher = pattern.matcher(str);
		return matcher.find();
	}

	/**
	 * Creates a regular expression pattern from entries in list
	 * @param list ArrayList of Strings with words to be used in pattern
	 * @return Pattern built from String entries in list
	 */
	public static Pattern regex(ArrayList<String> list)
	{
		String patternString = "\\b(" + StringUtils.join(list, "|") + ")\\b";
		return Pattern.compile(patternString);
	}

	public static void main(String[] args)
	{
		if (args.length != 1) {
			System.out.println("Usage: HedgeDetector <hedgeCueFile>");
			return;
		}

		Pattern cuePattern = loadCues(args[0]);
		Pattern slangPattern = loadSlang("../database/slang.txt");

		Matcher matcher;

		Scanner in = new Scanner(System.in);

		// Print csv header
		System.out.println(in.nextLine());

		while (in.hasNextLine()) {

			String line = nonSlang(in.nextLine(), slangPattern);
			matcher = cuePattern.matcher(line);

			while (matcher.find()) {
				StringBuilder taggedLine = new StringBuilder(line);
				taggedLine.insert(matcher.end(), "</strong>").insert(matcher.start(), "<strong>");
				System.out.println(taggedLine);
			}

		}

		in.close();
	}
}
