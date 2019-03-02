
/* Binary and Bitwise Operators */

import java.util.*;

public class BinaryBitwise {

    public static void main(String[] args) {

        //// Right shift operator
        int x = -1; // Recall int is store as a 32-bit signed integer

        System.out.println(x); // -1
        System.out.println(Integer.toBinaryString(x)); // 1 x 32

        int y = x >> 63; // Right shift keep sign

        System.out.println(y); // -1
        System.out.println(Integer.toBinaryString(y)); // 1 x 32

        int z = x >>> 63; // Right shift zero fill

        System.out.println(z); // -1
                               // reason

        int q = x << 63;

        //// Bitwise operation
        int op1 = 1;
        int op2 = 4;

        int a = op1 & op1; // Bitwise AND
        // Returns 1, Binary = 1, Hex = 1, Decimal = 1
        int b = op1 | op2; // Bitwise OR
        // Returns 5, Binary = 101, Hex = 5, Decimal = 5
        int c = op1 ^ op2; // Bitwise XOR
        // Same as above
        int d = ~op2; // Bitwise complement (i.e., inverse binary)
        // Returns -5, Binary = 11111111111111111111111111111011, Hex = fffffffb,
        // Decimal = -5

        int bitwiseArr[] = { a, b, c, d };

        for (int val : bitwiseArr) {
            System.out.printf("%n");
            System.out.println(val);
            System.out.println(String.format("%32s", Integer.toBinaryString(val)).replace(" ", "0")); // Binary
            System.out.printf("%x", val); // Hexidecimal
            System.out.printf("%n");
            System.out.printf("%d", val); // Decimal
            System.out.printf("%n");
        }

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
