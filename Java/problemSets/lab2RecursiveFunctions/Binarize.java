import java.util.*;
import java.util.ArrayList;

public class Binarize {

    // Constructor
    public Binarize() {
    }

    public void toBinary(int i) {

        //// Method to print an integer in binary format without Integer methods
        int initial = i;
        int quotient = 1;
        int remainder = 1;
        ArrayList<String> binary = new ArrayList<>(); // Is this an Integer method?

        while (quotient != 0) {
            quotient = i / 2;
            remainder = i % 2;
            i = quotient;
            binary.add(0, String.valueOf(remainder));
        }
        String binNum = String.join("", binary);
        System.out.println("Binary of " + initial + " is " + binNum);
    }

    public static void main(String args[]) {
        Binarize val = new Binarize();
        Scanner reader = new Scanner(System.in);
        val.toBinary(reader.nextInt());
    }

}