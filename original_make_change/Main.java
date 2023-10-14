/**
 * MAXEL Killian
 */

import java.util.*;

public class Main {

    // function to calculate the best change with the minimum number of coins
    // ITERATIVE GREEDY SOLUTION
    // greedy because we are using the coin that reduces the number of coins the most at each step
    public static List<Double> makeChangeBest(double[] coins, double amount) {
        // we must convert euros into cents to work on the same unit
        // 12.35 -> 1235
        int totalCents = (int) Math.round(amount * 100); // Convert the amount to cents
        // array to store the minimum number of coins for each amount
        double[] dp = new double[totalCents + 1];
        // we fill the array because we wish to use a placeholder to make comparisons
        // moreover the amount to pay can be gigantic
        Arrays.fill(dp, Double.MAX_VALUE);
        // for an amount of 0€, the required number of coins is 0
        dp[0] = 0;

        // dynamic approach to calculate the minimum number of coins needed
        // case for a coin = 0.1
        // we must find a required number of coins for an amount of 0.1
        for (double coin : coins) {
            // 0.1 so 10
            int coinCents = (int) Math.round(coin * 100); // Convert the coin value to cents
            // i=10, i < 1235, i++
            for (int i = coinCents; i <= totalCents; i++) {
                // if it's possible to reach 10 using this coin
                if (dp[i - coinCents] != Double.MAX_VALUE) {
                    // we seek the smallest/best number of coins needed
                    // between the one already collected and the new one
                    dp[i] = Math.min(dp[i], dp[i - coinCents] + 1);
                }
            }
        }

        // if there is no valid combination to make the amount, return an empty list
        // for instance, if we can't pay exactly the amount
        // in short it means that with our coins, the number of coins needed is not found
        if (dp[totalCents] == Double.MAX_VALUE) {
            return new ArrayList<>();
        }

        // we must now find the best change combination
        // because we checked before the minimum number of coins needed
        List<Double> bestChange = new ArrayList<>();
        int remaining = totalCents;
        while (remaining > 0) {
            boolean found = false;
            for (double coin : coins) {
                int coinCents = (int) Math.round(coin * 100); // Convert the coin value to cents
                if (remaining >= coinCents && dp[remaining - coinCents] == dp[remaining] - 1) {
                    bestChange.add(coin);
                    remaining -= coinCents;
                    found = true;
                    break;
                }
            }
            // if no valid coin can be used to reduce the remaining amount
            // no need to continue, we return an empty combination
            if (!found) {
                break;
            }
        }

        return bestChange;
    }

    // function to calculate the best change with the minimum number of coins
    // (ITERATIVE) ALL SOLUTIONS
    public static List<List<Double>> makeChangeAllIterative(double[] coins, double amount) {
        List<List<Double>> result = new ArrayList<>();
        int n = coins.length;
        // number of coins in coins as size
        // all set to 0 by default
        int[] coinIndexes = new int[n];

        /*
            coinIndexes[0] represents the count of the smallest coin in the array
            we need it to track how many times the smallest coin has been used in the current combination

            (amount / coins[0]) calculates the maximum number of times the smallest coin can be used to reach or exceed the target amount
            e.g : if smallest coin is 1 and amount is 10, then (amount / coins[0]) would be 10
         */

        // loop until we exhaust all possibilities
        // +1 because of 0
        while (coinIndexes[0] < (amount / coins[0]) + 1) {
            // calculate the sum of the current combination
            double sum = 0;
            for (int i = 0; i < n; i++) {
                sum += coins[i] * coinIndexes[i];
            }
            // if sum equals to target amount, add current combination to result
            if (sum == amount) {
                // we add the current combination to the result
                List<Double> combination = new ArrayList<>();
                for (int i = 0; i < n; i++) {
                    // add each coin to combination based on the count in coinIndexes
                    for (int j = 0; j < coinIndexes[i]; j++) {
                        combination.add(coins[i]);
                    }
                }
                result.add(combination);
            }
            int i = n - 1;
            // find the rightmost coin index that can be incremented
            while (i >= 0 && coinIndexes[i] >= (amount / coins[i])) {
                i--;
            }
            // if no rightmost coin index, then we leave the whole loop
            if (i < 0) {
                break;
            }
            // increment coin index at found index
            coinIndexes[i]++;
            // we reset all coin counts to the right of the incremented index
            for (int j = i + 1; j < n; j++) {
                coinIndexes[j] = 0;
            }
        }
        return result;
    }

    // function to calculate all possible combinations of coins for a given amount
    // RECURSIVE SOLUTION
    private static List<List<Double>> makeChangeAllRecursive(double[] coins, double amount, int start, List<Double> currentChange, List<List<Double>> result) {
        if (amount == 0) {
            // if the amount becomes zero, we've found a valid combination, add it to the result
            result.add(new ArrayList<>(currentChange));
        }

        for (int i = start; i < coins.length; i++) {
            int coinCents = (int) Math.round(coins[i] * 100); // Convert the coin value to cents
            if (amount >= coinCents) {
                currentChange.add(coins[i]);
                // explore all combinations recursively
                makeChangeAllRecursive(coins, amount - coinCents, i, currentChange, result);
                currentChange.remove(currentChange.size() - 1);
            }
        }
        return result;
    }

    public static void main(String[] args) {

        double[] coins = {5, 2, 1, 0.5, 0.2, 0.1, 0.05};
        double amount = 12.35;

        System.out.println("for amount="+amount);
        System.out.println("for coins={5, 2, 1, 0.5, 0.2, 0.1, 0.05}");

        int totalCents = (int) Math.round(amount * 100); // Convert the amount to cents

        // if remainder is not strictly 0, then combination ignored
        System.out.println("Best Change:");
        List<Double> bestChange = makeChangeBest(coins, amount);
        System.out.println(bestChange);

        double[] coins2 = {2, 1, 0.5, 0.2, 0.1, 0.05, 5};
        // if remainder is not strictly 0, then combination ignored
        System.out.println("Best Change2 (the set of coins order is changed) :");
        List<Double> bestChange2 = makeChangeBest(coins2, amount);
        System.out.println(bestChange2);

        /*

            ALL COMBINATIONS
            ITERATIVE SOLUTION

         */
        System.out.println("\nBecause iterative approach is memory greedy, we choose to work on a small set (amount=10, coins = {5,2,0.5}");
        System.out.println("\nAll Possible Changes in iterative (max for printing =  10 coins):");
        double amount1 = 10;
        double[] coins1 = {5,2,0.5};

        long startTime = System.nanoTime();
        List<List<Double>> allChanges1 = makeChangeAllIterative(coins1, amount1);
        long endTime = System.nanoTime();

        for (List<Double> change : allChanges1) {
            // for the printing, we choose to print only the
            if(change.size()<=10){
                System.out.println(change);
            }
        }
        System.out.println("nbr of combinations in iterative: "+allChanges1.size());
        long runtime = endTime - startTime;
        System.out.println("runtime for makeChangeAllIterative: " + runtime + " 10^-9 s");


        /*
            ALL COMBINATIONS
            RECURSIVE SOLUTION
         */

        /*

            to compare with iterative solution results

         */
        System.out.println("---\nTo compare with iterative approach we have: (amount=10, coins = {5,2,0.5}");
        System.out.println("\nAll Possible Changes in recursive (max for printing =  10 coins):");
        long startTime2 = System.nanoTime();
        List<List<Double>> allChanges2 = makeChangeAllRecursive(coins1, amount1*100, 0, new ArrayList<>(), new ArrayList<>());
        long endTime2 = System.nanoTime();
        for (List<Double> change : allChanges2) {
            // for the printing, we choose to print only the
            if(change.size()<=10){
                System.out.println(change);
            }
        }
        long runtime2 = endTime2 - startTime2;
        System.out.println("runtime for makeChangeAllRecursive: " + runtime2 + " 10^-9 s");

        System.out.println("nbr of combinations in recursive: "+allChanges2.size());
        System.out.println("nbr of combinations in iterative: "+allChanges1.size());


        // if remainder of a combination is not strictly 0, then not returned
        // combination with only coins of 0.5
        // ...
        // combination with only coins of 0.05
        // etc.
        System.out.println("\nWe go back to amount=12.35 and coins={5, 2, 1, 0.5, 0.2, 0.1, 0.05}");
        System.out.println("\nAll Possible Changes in recursive (max for printing =  10 coins):");
        List<List<Double>> result3 = new ArrayList<>();
        List<Double> currentChange3 = new ArrayList<>();
        List<List<Double>> allChanges3 = makeChangeAllRecursive(coins, totalCents, 0, currentChange3, result3);
        for (List<Double> change : allChanges3) {
            // for the printing, we choose to print only the
            if(change.size()<=10){
                System.out.println(change);
            }
        }
        System.out.println("nbr of combinations in recursive: "+allChanges3.size());

    }
}
