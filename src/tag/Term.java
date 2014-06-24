package tag;

/**
 * A term with its associated definitions
 * @author Javier Llaca
 */
public class Term
{
	/**
	 * The term
	 */
	private String term;

	/**
	 * Array containing definitions of the term
	 */
	private String[] definitions;

	/**
	 * Number of definitions associated with the term
	 */
	private int definitionCount;

	/**
	 * Initializes term to given parameter, definitionCount to 0 and definitions array
	 * @param term Term used for initialization
	 */
	public Term(String term)
	{
		this.term = term;
		this.definitions = new String[2];
		this.definitionCount = 0;
	}

	/**
	 * Adds a definition for this term
	 * @param definition Definition to be added
	 */
	public void addDefinition(String definition)
	{
		if (definitionCount < 2) {
			this.definitions[this.definitionCount++] = definition;
		}
	}

	/**
	 * Returns the definition
	 * @param index Index of definition in definition array
	 * @return Definition at index
	 */
	public String getDefinition(int index)
	{
		if (index >= definitionCount) {
			return null;
		}
		return this.definitions[index];
	}

	/**
	 * Returns a string with the term and its indexed definitions
	 * @return String representation of Term
	 */
	public String toString()
	{
		/* Use StringBuilder for better performance
		 * Concatenation (apppend) avoids building new Strings */
		StringBuilder str = new StringBuilder(this.term);
		for (int i = 0; i < this.definitionCount; i++) {
			str.append("\n");
			str.append(i);
			str.append(". ");
			str.append(this.definitions[i]);
		}
		return new String(str);
	}
}
