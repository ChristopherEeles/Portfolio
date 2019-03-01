/*-
 * StringBuilderGenBankSeq.java
 * 
 * Version 1.0
 * 
 * 2019-02-23
 */

/**
 * This class implementation over-rides the concatentate() method from the
 * Sequence() class to use the StringBuilder class for concatenating strings.
 */
public class StringBuilderGenBankSeq extends GenBankSequence {

    // Methods -----------------------------------------------

    /**
     * This method concatenates a string to the end of sequence N number of times
     * 
     * @param s       the string to concatenate to the end of sequence
     * @param n_times - the number of times string 's' will be appended to the end
     */
    @Override
    public void concatenate(String s, int n_times) {

        StringBuilder rawSeqBuilder = new StringBuilder(rawSequence);

        for (int i = 1; i <= n_times; i++) {
            System.out.println("Concatenating with String Builder " + i + " of " + n_times);
            rawSeqBuilder = rawSeqBuilder.append(s);
        }
    }
}