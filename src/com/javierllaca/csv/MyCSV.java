package com.javierllaca.csv;

import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import org.apache.commons.csv.CSVFormat;

import java.io.File;
import java.nio.charset.Charset;
import java.util.List;
import java.util.ArrayList;

/**
 * Wrapper class for Apache Commons CSV objects 
 *
 * @author Javier Llaca
 */
public class MyCSV {

  /**
   * The parser
   */
  private CSVParser parser;

  /**
   * The records of the parser. We keep track of them to avoid
   * using the parser iterator
   */
  private List<CSVRecord> records;

  /**
   * Constructs a MyCSV object from a csv file
   *
   * @param filename Path to csv file
   */
  public MyCSV(String filename) {
    try {
      this.parser = CSVParser.parse(
          new File(filename),
          Charset.forName("UTF-8"),
          CSVFormat.EXCEL.withHeader());
      this.records = this.parser.getRecords();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }

  /**
   * Returns a list with all the values of a column in the csv
   *
   * @param colName Column header name
   */
  public List<String> colValues(String colName) {
    List<String> values = new ArrayList<String>();
    for (CSVRecord record : this.records) {
      values.add(record.get(colName));
    }
    return values;
  }

  /**
   * Returns the string wrapped around quotes and escapes current quotes
   *
   * @param s String to be formatted
   */
  public static String formatString(String s) {
    return "\"" + s.replace("\"", "\"\"") + "\"";
  }
}
