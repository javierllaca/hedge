package com.javierllaca.hedge.driver;

import com.javierllaca.hedge.tag.Tagger;
import com.javierllaca.hedge.tag.TermNormalizer;

import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;

import opennlp.tools.sentdetect.SentenceModel;
import opennlp.tools.sentdetect.SentenceDetector;
import opennlp.tools.sentdetect.SentenceDetectorME;

/**
 * Driver for hedge detector program
 * @author Javier Llaca
 */
public class Main {
	public static void main(String[] args) throws Exception {
		if (args.length == 2) {
			// Setup sentece detection
			File modelFile = new File("en-sent.bin"); 
			SentenceModel model = new SentenceModel(modelFile);
			SentenceDetector detector = new SentenceDetectorME(model);

			// Setup hedge tagging and text normalization
			Tagger tagger = new Tagger(args[0], "strong");
			TermNormalizer normalizer = new TermNormalizer(args[1]);

			Scanner in = new Scanner(System.in);

			while (in.hasNextLine()) {
				String[] sentences = detector.sentDetect(in.nextLine());
				for (String sentence : sentences) {
					ArrayList<String> tags = tagger.tagLine(normalizer.normalizeLine(sentence));
					for (String tag : tags) {
						System.out.println(tag);
					}
				}
			}
			in.close();
		}
	}
}
