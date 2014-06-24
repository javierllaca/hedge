package tag;

import io.Input;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map.Entry;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

/**
 * Normalizes text according to a text database with term mappings
 * @author Javier Llaca
 */
public class TermNormalizer
{
	/**
	 * Stores term mappings
	 */
	private HashMap<String, String> termMap;

	/**
	 * Pattern to be matched
	 */
	private Pattern pattern;

	/**
	 * 
	 */
	public TermNormalizer(String filename)
	{
		termMap = new HashMap<String, String>();
		loadTerms(filename);
	}

	/**
	 * Loads terms and equivalences into an ArrayList object
	 * @param filename Path to  term file
	 */
	public void loadTerms(String filename)
	{
		Input in = new Input(filename);

		while (in.hasNextLine()) {
			String tok[] = in.readLine().split("\t");
			termMap.put(tok[0], tok[1]);
		}

		in.close();

		this.pattern = PatternUtils.createRegex(new ArrayList<String>(termMap.keySet()));
	}

	/**
	 * Returns a copy of str with  replaced by terms equivalences
	 * @param str Input string
	 * @return Term-normalized String
	 */
	public String normalizeLine(String line)
	{
		Matcher matcher = pattern.matcher(line);
		StringBuffer sb = new StringBuffer();

		while (matcher.find())
			matcher.appendReplacement(sb, termMap.get(matcher.group()));
		matcher.appendTail(sb);

		return new String(sb);
	}
}
