package detector;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.text.Normalizer;
import org.apache.commons.lang3.StringUtils;

/**
 * Detects and tags potential hedge cues in text from stdin
 * @author Javier Llaca
 */
public class HedgeDetector
{
	public static ArrayList<String> cues;
	public static Pattern pattern;
	public static Matcher matcher;
	public static int hedgeCount = 0;

	/** 
	 * Loads hedge cues in file into an ArrayList object
	 * @param filename Path to hedge cue file
	 */
	public static void loadCues(String filename)
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
		} catch (FileNotFoundException e) {};
	}

	/**
	 * Returns copy of str with normalized non-ASCII characters
	 * @param str Input string
	 */
	public static String normalized(String str)
	{
		return Normalizer.normalize(str, Normalizer.Form.NFD).replaceAll("[^\\p{ASCII}]", "");
	}

	/**
	 * Determines whether str contains characters with acute accent
	 * @param str Input string
	 */
	public static boolean containsAcuteAccent(String str)
	{
		Pattern pattern = Pattern.compile("[ÁÉÍÓÚáéíóú]");
		Matcher matcher = pattern.matcher(str);
		return matcher.find();
	}

	/**
	 * Creates a regular expression pattern from all hedge cues
	 */
	public static void createRegex()
	{
		String patternString = "\\b(" + StringUtils.join(cues, "|") + ")\\b";
		pattern = Pattern.compile(patternString);
	}

	public static void main(String[] args)
	{
		if (args.length != 1) {
			System.out.println("Usage: HedgeDetector <hedgeCueFile>");
			return;
		}

		loadCues(args[0]);
		createRegex();

		Scanner in = new Scanner(System.in);

		while (in.hasNextLine()) {
			String line = in.nextLine();
			matcher = pattern.matcher(line);
			StringBuffer sb = new StringBuffer();
			while (matcher.find()) {
				hedgeCount++;
				matcher.appendReplacement(sb, 
						"<strong>" + matcher.group() + "</strong>");
			}
			matcher.appendTail(sb);
			System.out.println(sb);
		}

		in.close();
	}
}
