package tag;

public class Term
{
	private String term;
	private String[] definitions;
	private int definitionCount;

	public Term(String term)
	{
		this.term = term;
		this.definitions = new String[2];
		this.definitionCount = 0;
	}

	public void addDefinition(String definition)
	{
		if (definitionCount < 2) {
			this.definitions[this.definitionCount++] = definition;
		}
	}

	public String getDefinition(int i)
	{
		if (i >= definitionCount) {
			return null;
		}
		return this.definitions[i];
	}

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
	
	public static void main(String[] args)
	{
		Term t = new Term("dog");
		t.addDefinition("canine animal");
		t.addDefinition("derrogatory adjective for a person");
		t.addDefinition("garbage...");		// nothing is added
		System.out.println(t);
		System.out.println(t.getDefinition(3));	// prints "null"
	}
}
