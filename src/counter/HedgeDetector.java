package counter;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import org.apache.commons.lang3.StringUtils;

public class HedgeDetector
{
	public static ArrayList<String> cues;
	public static Pattern pattern;
	public static Matcher matcher;
	public static int hedgeCount = 0;

	// Loads hedge cues in file into an ArrayList object
	public static void loadCues(String filename)
	{
		try {
			File words = new File(filename);
			Scanner db = new Scanner(words);

			cues = new ArrayList<String>();
			while (db.hasNextLine()) {
				String line = db.nextLine().trim();
				if (!line.isEmpty()) // ignore blank lines
					cues.add(line);
			}

			db.close();
		} catch (FileNotFoundException e) {};
	}

	// Creates a regular expression pattern from all hedge cues
	public static void createRegex()
	{
		String patternString = "\\b(" + StringUtils.join(cues, "|") + ")\\b";
		pattern = Pattern.compile(patternString);
	}

	public static void main(String args[])
	{
		if (args.length != 2) {
			System.out.println("Usage: SimpleCounter <hedgeCueFile> <inputFile>");
			return;
		}

		loadCues(args[0]);
		createRegex();

		try {
			File file = new File(args[1]);
			Scanner in = new Scanner(file);

			while (in.hasNextLine()) {
				String line = in.nextLine();
				matcher = pattern.matcher(line);
				StringBuffer sb = new StringBuffer();
				while (matcher.find()) {
					hedgeCount++;
					matcher.appendReplacement(sb, "<h>" + matcher.group() + "</h>");
				}
				matcher.appendTail(sb);
				System.out.println(sb);
			}

			System.out.println("\nHedges: " + hedgeCount);
			in.close();
		} catch (FileNotFoundException e) {};
	}
}
