package driver;

import tag.Tagger;
import tag.TermNormalizer;

import java.util.ArrayList;
import java.util.Scanner;

public class Main
{
	public static void main(String[] args)
	{
		Tagger tagger = new Tagger(args[0], "tag");
		Scanner in = new Scanner(System.in);
		TermNormalizer normalizer = new TermNormalizer("../database/slang.txt");

		while (in.hasNextLine()) {
			ArrayList<String> taggedLines = tagger.tagLine(normalizer.normalizeLine(in.nextLine()));
			for (String tag : taggedLines)
				System.out.println(tag);
		}
	}
}
