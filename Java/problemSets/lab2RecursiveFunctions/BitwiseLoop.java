import java.util.*;
import java.io.*;

public class BitwiseLoop {
    public static void main(String args[]) {
        System.out.println("Enter an int to see binary version: ");
        Scanner input = new Scanner(System.in);
        int n;
        while ((n = input.nextInt()) != 0) {
            System.out.println(String.format("%32s", Integer.toBinaryString(n)).replace(" ", "0"));
        }

        System.out.println("Shift -1 >>> ? ");
        Scanner input2 = new Scanner(System.in);
        int n2;
        while ((n2 = input2.nextInt()) != 0) {
            int m = -1 >>> n2; // Adds a n2 zeros at index 0, shifts values right.
            System.out.println(String.format("%32s", Integer.toBinaryString(m)).replace(" ", "0"));
        }

        System.out.println("Shift -1 >> ? ");
        Scanner input3 = new Scanner(System.in);
        int n3; // Adds n3 ones at index 0, shifts values right.
        while ((n3 = input3.nextInt()) != 0) {
            int m1 = -1 >> n3;
            System.out.println(String.format("%32s", Integer.toBinaryString(m1)).replace(" ", "0"));
        }

        System.out.println("Shift -1 << ? ");
        Scanner input4 = new Scanner(System.in);
        int n4;
        while ((n4 = input4.nextInt()) != 0) {
            int m2 = -1 << n4; // Adds n4 zeros at index -1, shifts values left.
            System.out.println(String.format("%32s", Integer.toBinaryString(m2)).replace(" ", "0"));
        }

    }
}
