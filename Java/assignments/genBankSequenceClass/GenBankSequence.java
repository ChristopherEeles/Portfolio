/**
 *  I declare that the attached assignment and source code are in my own work in accordance
 *  with Seneca Academic Policy. No part of this assignment or source dode have been copied
 *  manually or electronically from any source (including websites) or distrubted to other 
 *  students.
 *  
 *  Name: Christopher Eeles
 *  Student ID: 130 079 183
 * */

/*-
 * GenBankSequence
 *
 * Version 1
 *
 * 2019-02-2019 
 * 
 */

/**
 * A class to store information from GenBank nucleotide/protein files
 * GenBankSequence class (child) inherits from Sequence class (parent)
 */
public class GenBankSequence extends Sequence {

    // Variables -------------------------------------------------
    private String locus; // Variable to hold gene locus
    private String accessionNum; // Variable to hold accession number
    private String definition; // Variable to hold definition
    private String source; // Variable to hold information source

    // Constructors -----------------------------------------------

    /**
     * Instantiates GenBankSequence with all variables set to null
     */
    public GenBankSequence() {
    }

    /**
     * Instantiates GenBankSequence with only locus and accessionNum
     */
    public GenBankSequence(String locus, String accessionNum) {
        this.locus = locus; // Sets locus class variable to locus value argument
        this.accessionNum = accessionNum; // Sets accessionNum class variable to accessionNum value argument
    }

    /**
     * Instantiates GenBankSequence with all variable values set
     */
    public GenBankSequence(String locus, String accessionNum, String definition, String source) {
        this(locus, accessionNum);
        this.definition = definition;
        this.source = source;
    }

    // Getter/Setter Methods -------------------------------------

    /**
     * Retrieve the locus of the gene in this object
     * 
     * @return this instance of the locus
     */
    public String getLocus() {
        if (this.locus == null) {
            return warning("locus");
        } else {
            return this.locus;
        }
    }

    /**
     * Retrieve the accession number of the sequence in this object
     * 
     * @return
     */
    public String getAccessionNum() {
        if (this.accessionNum == null) {
            return warning("accessionNum");

        } else {
            return this.accessionNum;
        }
    }

    /**
     * Retrieve the definition of this object
     * 
     * @return this instance of the definition in this object
     */
    public String getDefinition() {
        if (this.definition == null) {
            return warning("definition");
        } else {
            return this.definition;
        }
    }

    /**
     * Retrieve the source of this object
     * 
     * @return this instance of the source in this object
     */
    public String getSource() {
        if (this.source == null) {
            return warning("source");
        } else {
            return source;
        }
    }

    /**
     * Set the locus value for this object
     * 
     * @param locus - the locus value you want to assign
     */
    public void setLocus(String locus) {
        this.locus = locus;
    }

    /**
     * Set the accessionNum value for this object
     * 
     * @param accessionNum - the accessionNum value you want to assign
     */
    public void setAccessionNum(String accessionNum) {
        this.accessionNum = accessionNum;
    }

    /**
     * Set the definition value for this object
     * 
     * @param definition - the definition value you want to assign
     */
    public void setDefinition(String definition) {
        this.definition = definition;
    }

    /**
     * Set the source value for this object
     * 
     * @param source - the source value you want to assign
     */
    public void setSource(String source) {
        this.source = source;
    }

    // Methods ---------------------------------------------------

    /**
     * This method overrides toString() from java.lang.Object
     * 
     * @return locus, accessionNum, definition, source values from this object
     */
    @Override
    public String toString() {
        String objContents = ("Locus: " + this.getLocus() + "\n" + "Definition: " + this.getDefinition() + "\n"
                + "Accession Number: " + this.getAccessionNum() + "\n" + "Source: " + this.getSource() + "\n");

        return objContents;
    }

    /**
     * This method returns warnings if getter for an uninitialized variable is
     * called
     * 
     * @return warn - A warning about which variable was null
     */
    private String warning(String var) {
        String warn = ("WARNING! The variable " + var + " has not been initialized, please use the " + var
                + " setter to assign a string value.");
        return warn;
    }
}