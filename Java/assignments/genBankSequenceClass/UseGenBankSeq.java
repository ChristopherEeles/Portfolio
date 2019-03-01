/*-
 * UseGenBankSeq
 *
 * Version 1
 *
 * 2019-02-2019 
 * 
 */

/**
 * A main class to intialize GenBankSequence objects and test their methods.
 */
public class UseGenBankSeq {

    /**
     * Main class to execute Java code
     */
    public static void main(String[] args) {

        // Empty constructor ---------------------------------------
        System.out.println("\nGenBankSequence Empty Constructor");
        GenBankSequence Seq0 = new GenBankSequence();

        System.out.println("\nEmpty GenBankSequence object:\n" + Seq0.toString());

        /**
         * GenBank results for Homo sapiens 5-HT6 serotonin receptor mRNA Data retrieved
         * Retrieved from https://www.ncbi.nlm.nih.gov/nuccore/L41147.1
         */
        Seq0.setLocus("HUM5HSR 1984 bp mRNA linear PRI 21-MAR-1996");
        Seq0.setAccessionNum("L41147");
        Seq0.setDefinition("Homo sapiens 5-HT6 serotonin receptor mRNA, complete cds.");
        Seq0.setSource("Homo sapiens (human)");

        System.out.println("Complete Homo sapiens Serotonin 5-TH6R mRNA:\n" + Seq0.toString());

        // Two paramater constructor -------------------------------
        System.out.println("GenBankSequence Two Argument Constructor\n");

        /**
         * GenBank results for Homo sapiens alpha adrenergic receptor subtype alpha 1a
         * Retrieved from https://www.ncbi.nlm.nih.gov/nuccore/S70782.1
         */
        GenBankSequence Seq2 = new GenBankSequence("S70782 1776 bp mRNA linear PRI 04-MAY-2000", "S70782");

        System.out.println("Missing two arguments for Homo sapiens Adrenergic A1aR mRNA:  " + Seq2.toString());

        Seq2.setDefinition("Homo sapiens alpha adrenergic receptor subtype alpha 1a mRNA, complete cds.");
        Seq2.setSource("Homo sapiens (human)");

        System.out.println("Complete Homo sapiens Adrenergic A1aR mRNA:  " + Seq2.toString());

        // Four parameter constructor ------------------------------
        System.out.println("GenBankSequence Four Argument Constructor\n");

        /**
         * GenBank results for Homo sapiens dopamine receptor D1 (DRD1) Retrieved from
         * https://www.ncbi.nlm.nih.gov/nuccore/NM_000794.5
         */
        GenBankSequence Seq4 = new GenBankSequence("NM_000794 4031 bp mRNA linear PRI 23-DEC-2018", "NM_000794",
                "Homo sapiens dopamine receptor D1 (DRD1), mRNA.", "Homo sapiens (human)\n");

        System.out.println("Complete Homo sapiens Dopamine DRD1 mRNA:\n" + Seq4.toString());
    }

}