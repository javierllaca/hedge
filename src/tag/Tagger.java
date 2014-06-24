package tag;

import io.Input;

import java.util.ArrayList;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

/**
 * Tags lines of text according to a text database
 * @author Javier Llaca
 */
public class Tagger
{
	/**
	 * String embedded in tag
	 * Format: <tag>text</tag>
	 */
	private String tag;

	/**
	 * Pattern to be tagged
	 */
	private Pattern pattern;

	/**
	 * Constructor
	 */
	public Tagger(String filename, String tag)
	{
		this.tag = tag;
		loadCues(filename);
	}

	/** 
	 * Loads hedge cues in file into an ArrayList object
	 * @param filename Path to hedge cue file
	 * @return Regular expression pattern built from all hedge cues
	 */
	public void loadCues(String filename)
	{
		Input in = new Input(filename);
		ArrayList<String> cues = new ArrayList<String>();

		while (in.hasNextLine()) {
			String line = in.readLine().trim();
			if (!line.isEmpty()) {
				cues.add(line);
				if (PatternUtils.containsAcuteAccent(line))
					cues.add(PatternUtils.normalizeEncoding(line));
			}
		}

		in.close();

		this.pattern = PatternUtils.createRegex(cues);
	}

	/**
	 * Returns an ArrayList containing all versions of tagged line
	 * @param line Input line
	 */
	public ArrayList<String> tagLine(String line)
	{
		ArrayList<String> tags = new ArrayList<String>();
		Matcher matcher = this.pattern.matcher(line);

		while (matcher.find()) {
			StringBuilder tag = new StringBuilder(line);
			tags.add(new String(tag.insert(matcher.end(), "</" + this.tag + ">").insert(
						matcher.start(), "<" + this.tag + ">")));
		}

		return tags;
	}
}
