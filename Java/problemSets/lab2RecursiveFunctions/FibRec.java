
// Recursive Fibonacci

import java.util.*;

public class FibRec {
    // Variables
    ArrayList<Integer> fibonacci = new ArrayList<Integer>();
    int maxFib;

    // Constructor
    public FibRec() {
    }

    // Methods
    public int fibR(int num) {
        if (num <= 1) {
            return 1;
        } else {
            return fibR(num - 1) + fibR(num - 2);
        }
    }

    public int[] fibSeries(int num) {
        int fib[] = new int[num];

        for (int i = 0; i < num; i++) {
            fib[i] = fibR(i);
        }
        return fib;
    }

    public static void main(String[] args) {
        FibRec fibRec = new FibRec();

        int fibSeriesRec[] = fibRec.fibSeries(10);

        for (int i = 0; i < fibSeriesRec.length; i++) {
            System.out.print(" " + fibSeriesRec[i] + " ");
        }

    }

}