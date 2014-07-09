package com.javierllaca.io;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/**
 * Wrapper class for file input
 * @author Javier Llaca
 */
public class Input {
	/**
	 * File to read from
	 */
	private File file;

	/**
	 * Reading object
	 */
	private Scanner in;

	/**
	 * Constructor
	 * @param filename Path of file to be read
	 */
	public Input(String filename) {
		try {
			file = new File(filename);
			in = new Scanner(file);
		} catch (FileNotFoundException e) { e.printStackTrace(); }
	}

	/**
	 * Determines whether there is another line in input
	 * @return true if there is at least one line, false otherwise
	 */
	public boolean hasNextLine() {
		return in.hasNextLine();
	}

	/**
	 * Returns the next line in input
	 */
	public String readLine() {
		return in.nextLine();
	}

	/**
	 * Closes the Scanner object
	 */
	public void close() {
		in.close();
	}
}
