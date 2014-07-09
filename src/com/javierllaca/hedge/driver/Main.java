package com.javierllaca.hedge.driver;

import com.javierllaca.hedge.tag.Tagger;
import com.javierllaca.hedge.tag.TermNormalizer;

import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

import opennlp.tools.sentdetect.*;

public class Main {
	public static void main(String[] args) throws Exception {
		TermNormalizer normalizer = new TermNormalizer("../database/slang");
		Tagger tagger = new Tagger(args[0], "strong");
		Scanner in = new Scanner(System.in);

		File modelFile = new File("en-sent.bin"); 
		SentenceModel model = new SentenceModel(modelFile);

		SentenceDetector detector = new SentenceDetectorME(model);

		/* Print csv header */
		System.out.println("sentence,term,definition1,definition2");

		while (in.hasNextLine()) {
			String[] results = detector.sentDetect(in.nextLine());
			for (String result : results) {
				ArrayList<String> taggedLines = tagger.tagLine(normalizer.normalizeLine(result));
				for (String taggedLine : taggedLines) {
					System.out.println(taggedLine);
				}
			}
		}
		in.close();
	}
}
