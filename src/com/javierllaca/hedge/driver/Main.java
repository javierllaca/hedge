package com.javierllaca.hedge.driver;

import com.javierllaca.hedge.tag.Tagger;
import com.javierllaca.hedge.tag.TermNormalizer;

import java.util.ArrayList;
import java.util.Scanner;

public class Main
{
	public static void main(String[] args)
	{
		Tagger tagger = new Tagger(args[0], "strong");
		Scanner in = new Scanner(System.in);
		TermNormalizer normalizer = new TermNormalizer("../database/slang.txt");

		// Print csv header
		System.out.println(in.nextLine());

		while (in.hasNextLine()) {
			ArrayList<String> taggedLines = tagger.tagLine(normalizer.normalizeLine(in.nextLine()));
			for (String taggedLine : taggedLines)
				System.out.println(taggedLine);
		}
	}
}
