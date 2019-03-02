
// Greated Common Divisor

import java.util.*;

public class GCD {

    // Variables
    int greatestCD;

    // Constructor
    public GCD() {
    }

    // Methods
    public int gcd(int a, int b) {

        int[] inputs = { a, b };

        Arrays.sort(inputs);

        a = inputs[1];
        b = inputs[0];

        if (b == 0) {
            return a;
        } else {
            return gcd(b, (a % b));
        }
    }

    public static void main(String[] args) {
        GCD calculateGCD = new GCD();

        System.out.println(calculateGCD.gcd(128, 552));
    }
}