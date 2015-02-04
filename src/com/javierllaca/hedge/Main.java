package com.javierllaca.hedge;

import com.javierllaca.collect.Pair;
import com.javierllaca.text.Tagger;
import com.javierllaca.text.TermNormalizer;

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
			File modelFile = new File("bin/en-sent.bin"); 
			SentenceModel model = new SentenceModel(modelFile);
			SentenceDetector detector = new SentenceDetectorME(model);

			// Setup slang normalization
			TermNormalizer normalizer = new TermNormalizer(args[0]);

			// Setup hedge tagging
			Tagger tagger = new Tagger(args[1], "strong");

			Scanner in = new Scanner(System.in);

			while (in.hasNextLine()) {

				String[] sentences = detector.sentDetect(in.nextLine());

				for (String sentence : sentences) {

					ArrayList<Pair<String,String>> tags = tagger.tagLine(
							normalizer.normalizeLine(sentence));

					for (Pair<String,String> tag : tags) {

						System.out.println("\"" + tag.first() + "\",\"" + 
								tag.second().replace("\"", "\"\"") + "\"");
					}
				}
			}

			in.close();

		} else {
			System.out.println("Usage: java Main <slangPath> <hedgePath>");
		}
	}
}
