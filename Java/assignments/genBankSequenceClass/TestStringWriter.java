
/*-
 * TestStringWriter.java
 * 
 * Version 1.0
 * 
 * 2019-02-23
 */

import java.util.*;

/**
 * A main class to intialize StringWriterGenBankSeq objects and test the
 * execution time of repated sequence concatenations using the concatate()
 * method.
 */
public class TestStringWriter {
    public static void main(String[] args) {

        // Variables -----------------------------------------------------------
        StringWriterGenBankSeq test = new StringWriterGenBankSeq();
        ArrayList<Long> times = new ArrayList<Long>(); // Stores time results for each file
        ArrayList<String> files = new ArrayList<String>(); // Stores the file names
        String typeObject = "StringWriterSeq"; // To generalize the print statements

        // Running testConcatendate() for each of five files ---------------------------
        for (int i = 0; i < 5; i++) {

            /**
             * Concatenates appropriate numbers to start of file name and adds them to
             * ArrayList files
             */
            files.add(Math.round(Math.pow(10, i)) + "k_Sample.txt");
            /**
             * Prints the number of iterations, file name and object class for each
             * execution of test.Concatenate()
             */
            System.out.println(Math.round(Math.pow(10, 5 - i)) + " times for " + files.get(files.size() - 1)
                    + " data for" + typeObject);

            /**
             * Passes file name and number of iterations as arguments to testConcatenate for
             * the five required files, then adds the resulting runtime to the times
             * ArrayList
             */
            times.add((test.testConcatenate(files.get(files.size() - 1), (int) Math.round((Math.pow(10, 5 - i))))));

        }
        // Output results
        // ---------------------------------------------------------------------------
        /**
         * Prints the number of iterations, file name and object class for each
         * execution of test.Concatenate()
         */
        for (int i = 0; i < 5; i++) {
            System.out.println(Math.round(Math.pow(10, 5 - i)) + " iterations for " + files.get(i) + " of the "
                    + typeObject + " took " + times.get(i) + " nanoseconds, or approximately "
                    + (times.get(i) / Math.pow(10, 6)) + " milliseconds");
        }
    }
}