package tag;

import io.Input;

import java.util.ArrayList;
import java.util.List;
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
	 * Pattern to be queried
	 */
	private Pattern pattern;

	/**
	 * Initializes term map and creates a Pattern from terms in file
	 * @param filename Path to term file
	 */
	public TermNormalizer(String filename)
	{
		termMap = new HashMap<String, String>();
		List<String> terms = termListFromFile(filename);
		this.pattern = PatternUtils.createRegexFromList(terms);
	}

	/**
	 * Returns a list with terms in file
	 * @param filename Path to term file
	 * @return List with terms
	 */
	public List<String> termListFromFile(String filename)
	{
		Input in = new Input(filename);
		while (in.hasNextLine()) {
			String tok[] = in.readLine().split("\t");
			termMap.put(tok[0], tok[1]);
		}
		in.close();
		return new ArrayList<String>(termMap.keySet());
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
