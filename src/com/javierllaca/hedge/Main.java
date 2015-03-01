package com.javierllaca.hedge;

import com.javierllaca.csv.MyCSV;
import com.javierllaca.collect.Pair;
import com.javierllaca.io.Input;
import com.javierllaca.text.PatternUtils;
import com.javierllaca.text.Tagger;
import com.javierllaca.text.TermNormalizer;

import java.io.File;
import java.util.List;

import opennlp.tools.sentdetect.SentenceModel;
import opennlp.tools.sentdetect.SentenceDetector;
import opennlp.tools.sentdetect.SentenceDetectorME;

/**
 * Driver for hedge tagging program
 *
 * @author Javier Llaca
 */
public class Main {

  public static void main(String[] args) throws Exception {

    if (args.length == 2) {

      // Sentece detection
      SentenceDetector detector = new SentenceDetectorME(
          new SentenceModel(
            new File("bin/en-sent.bin")));

      // Slang normalization
      TermNormalizer normalizer = new TermNormalizer(
          args[0],
          "slang",
          "normal");

      // Hedge tagging
      Tagger tagger = new Tagger(
          "strong", 
          PatternUtils.conjunctionRegex(
            PatternUtils.normalizedList(
              (new MyCSV(args[1])).colValues("hedge"))));

      Input in = new Input(System.in);
      String line;

      while ((line = in.readLine()) != null) {

        for (String sentence : detector.sentDetect(line)) {

          List<Pair<String,String>> tags = 
            tagger.tagLine(normalizer.normalizeLine(sentence));

          for (Pair<String,String> tag : tags) {

            System.out.println(
                MyCSV.formatString(tag.first()) + "," +
                MyCSV.formatString(tag.second()));
          }
        }
      }

      in.close();

    } else {
      System.out.println("Usage: java Main <slang csv> <hedge csv>");
    }
  }
}
