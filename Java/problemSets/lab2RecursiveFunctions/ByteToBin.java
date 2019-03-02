import java.util.*;
import java.io.*;

public class ByteToBin {
    // Constructor
    public ByteToBin() {
    }

    public static void main(String args[]) {
        Scanner userIn = new Scanner(System.in);

        byte b1 = userIn.nextByte();
        String s1 = String.format("%8s", Integer.toBinaryString(b1 & 0xFF)).replace(' ', '0');
        System.out.println(s1);

    }
}

// Input 127 returns 01111111
// Input 128 returns Exception: "Value out of range"
// This is due to the limit for the byte (8 bits) data type to -128 to 127
// To cast one primitive to another you can specify the desired type in ( )
// For example byte b1 = (byte) 127, converts into to byte