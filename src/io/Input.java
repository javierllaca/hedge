package io;

import java.io.File;
import java.io.FileNotFoundException;

import java.util.Scanner;

/**
 * Wrapper class for manipulating input
 * @author Javier Llaca
 */
public class Input
{
	/**
	 * File to read from
	 */
	private File file;

	/**
	 * Reading object
	 */
	private Scanner in;

	public Input(String filename)
	{
		try {
			file = new File(filename);
			in = new Scanner(file);
		} catch (FileNotFoundException e) {
			System.out.println(e);
		};
	}

	/**
	 * Determines whether there is another line in input
	 * @return true if there is at least one line, false otherwise
	 */
	public boolean hasNextLine()
	{
		return in.hasNextLine();
	}

	/**
	 * Returns the next line in input
	 */
	public String readLine()
	{
		return in.nextLine();
	}

	/**
	 * Closes the Scanner object
	 */
	public void close()
	{
		in.close();
	}
}
