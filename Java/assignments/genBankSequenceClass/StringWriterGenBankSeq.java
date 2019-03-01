
/*-
 * StringWriterGenBankSeq.java
 * 
 * Version 1.0
 * 
 * 2019-02-23
 */

import java.io.StringWriter;

/**
 * This class implementation over-rides the concatentate() method from the
 * Sequence() class to use the StringBuilder class for concatenating strings.
 */
public class StringWriterGenBankSeq extends GenBankSequence {

    // Variables ---------------------------------------------

    // Methods -----------------------------------------------

    /**
     * This method overrides Sequence.concatenate() to use the StringWriter class
     * for concatenating the strings in the object.
     * 
     * @param s       the string to concatenate to the end of sequence
     * @param n_times - the number of times string 's' will be appended to the end
     */
    @Override
    public void concatenate(String s, int n_times) {

        /**
         * Creates a StringWriter object with elements equal to the total number of
         * characters of the entire concatenation
         * 
         * @param rawSequence.length() - number of characters in rawSequence.
         * @param s.length()           - number of characters in string to concatenate.
         * @param n_times              - number of times string 's' will be appended
         */
        StringWriter StringWriterOfrawSequence = new StringWriter();
        StringWriterOfrawSequence.write(rawSequence);

        for (int i = 1; i <= n_times; i++) {
            System.out.println("Concatenating " + i + " of " + n_times);
            StringWriterOfrawSequence.write(s);
        }
    }
}