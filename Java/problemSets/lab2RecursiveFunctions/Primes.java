import java.util.*;

public class Primes {

    // Variables
    ArrayList<Integer> primes = new ArrayList<Integer>();

    // Constructor
    public Primes() {
    }

    // Methods
    public boolean isPrime(int num) {
        Collections.sort(primes);
        if (num == 0 || num == 2) {
            return false;
        } else if (num == 1) {
            primes.add(0, 1);
            return true;
        }
        for (int i = 2; i <= num / 2; i++) {
            if (num % i == 0)
                return false;
        }

        if (primes.contains(num) == true) {
            return true;
        } else {
            for (int j = 0; j < primes.size(); j++) {
                if (num > primes.get(j)) {
                    continue;
                } else if (num < primes.get(j)) {
                    primes.add(j, num);
                    return true;
                }
            }
            primes.add(num);
        }
        return true;
    }

    public void getPrimes() {
        System.out.print("Primes discovered are: " + primes);
    }

    public void setPrimes(int maxVal) {

    }

    // Main

    public static void main(String[] args) {
        Primes primesList = new Primes();

        System.out.println("Enter a number to check if it is prime:");
        Scanner userInput = new Scanner(System.in);

        while (userInput.hasNextInt()) {
            System.out.println(primesList.isPrime(userInput.nextInt()));
        }

        primesList.getPrimes();

    }
}