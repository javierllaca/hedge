package com.javierllaca.io;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.InputStream;
import java.io.InputStreamReader;

/**
 * Wrapper class for file input
 *
 * @author Javier Llaca
 */
public class Input {

  /**
   * The input reader
   */
  private BufferedReader in;

  /**
   * Constructor for file inputs
   *
   * @param filename Path of file to be read
   */
  public Input(String filename) {
    try {
      this.in = new BufferedReader(new FileReader(new File(filename)));
    } catch (Exception e) { 
      e.printStackTrace();
    }
  }

  /**
   * Constructor for stdin (or other stream) input
   *
   * @param stream Stream to be read
   */
  public Input(InputStream stream) {
    this.in = new BufferedReader(new InputStreamReader(stream));
  }

  /**
   * Returns the next line in input
   */
  public String readLine() {
    try {
      return this.in.readLine();
    } catch (Exception e) {
      e.printStackTrace();
    } return null;
  }

  /**
   * Closes the reader
   */
  public void close() {
    try {
      this.in.close();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
