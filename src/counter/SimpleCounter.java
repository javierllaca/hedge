package counter;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

public class SimpleCounter
{
	public static ArrayList<String> cues;
	public static int hedgeCount;

	public static void loadCues(String filename)
	{
		try {
			File words = new File(filename);
			Scanner db = new Scanner(words);

			cues = new ArrayList<String>();
			while (db.hasNextLine())
				cues.add(db.nextLine());

			db.close();
		} catch (FileNotFoundException e) {};
	}

	public static String tag(String s, String cue, String tag)
	{
		String lhs = insert(s, "<" + tag + ">", s.indexOf(cue));
		return insert(lhs, "</" + tag + ">", lhs.indexOf(cue) + cue.length());
	}

	public static String insert(String s1, String s2, int index)
	{
		return s1.substring(0, index) + s2 + s1.substring(index);
	}

	public static void main(String args[])
	{
		if (args.length != 2) {
			System.out.println("Usage: java counter/SimpleCounter <hedgeCueFile> <data>");
			return;
		}

		try {
			loadCues(args[0]);
			hedgeCount = 0;

			File file = new File(args[1]);
			Scanner in = new Scanner(file);

			while (in.hasNextLine()) {
				String line = in.nextLine();
				for (String cue : cues) {
					if (line.contains(cue)) {
						hedgeCount++;
						line = tag(line, cue, "tag");
					}
				}
				System.out.print(line);
			}

			System.out.println(hedgeCount);

			in.close();
		} catch (FileNotFoundException e) {};
	}
}
