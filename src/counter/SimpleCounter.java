package counter;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.LinkedList;

public class SimpleCounter
{
	public static LinkedList<String> cues;
	public static int hedgeCount;

	public static void loadCues(String filename)
	{
		try {
			File words = new File(filename);
			Scanner db = new Scanner(words);

			cues = new LinkedList<String>();
			while (db.hasNextLine())
				cues.add(db.nextLine());

			db.close();
		} catch (FileNotFoundException e) {};
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
				String[] line = in.nextLine().split("\\s+");
				for (String tok : line)
					if (cues.contains(tok))
						hedgeCount++;
			}

			System.out.println(hedgeCount);

			in.close();
		} catch (FileNotFoundException e) {};
	}
}
