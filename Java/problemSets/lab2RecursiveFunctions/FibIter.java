
// Iterative Fibonacci

import java.util.*;

public class FibIter {

    // Variables
    ArrayList<Integer> fibonacci = new ArrayList<Integer>();
    int maxFib;

    // Constructor
    public FibIter() {
    }

    // Methods
    private void fib(int num) {
        maxFib = num;
        fibonacci.clear();
        for (int i = 0; i < (num); i++) {
            switch (i) {
            case 0:
                fibonacci.add(0, 1);
                continue;
            case 1:
                fibonacci.add(1, 1);
                continue;
            }
            fibonacci.add(i, (fibonacci.get(i - 2) + fibonacci.get(i - 1)));
        }
    }

    private void getFib() {
        System.out.println("The first " + maxFib + " numbers of the Fibonacci sequence are: " + fibonacci);
    }

    public static void main(String[] args) {
        FibIter fib1 = new FibIter();

        System.out.println("How many values of the Fibonacci sequence would you like to see?");
        Scanner userIn = new Scanner(System.in);

        while (userIn.hasNextInt()) {
            fib1.fib(userIn.nextInt());
            fib1.getFib();
        }

    }

}
