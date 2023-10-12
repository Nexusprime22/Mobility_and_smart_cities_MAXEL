# modify program 5 or program 4 so that the best calculated
# solution is stored in a solution table. Evaluate the computation time
# saved and the display savings.

import time

# Function to calculate all combinations of coins to make a specific amount
def calculate_change_combinations(coins, amount):
    # Convert euro amounts to cents for calculations
    amount_cents = int(amount * 100)
    coin_values_cents = [int(coin * 100) for coin in coins]

    # Initialize a list to store combinations and their counts
    combinations = []
    stack = [(0, [], 0)]  # (current amount in cents, current combination, current coin index)

    best_solution = [[] for i in range(len(coins))]

    while stack:
        current_amount, current_combination, current_coin_index = stack.pop()

        # If the current combination sums up to the target amount, add it to the list
        if current_amount == amount_cents:
            if len(current_combination) < len(best_solution):
                best_solution = current_combination

        # If the current amount is less than the target amount and there are more coins to consider
        elif current_amount < amount_cents and current_coin_index < len(coin_values_cents):
            coin = coin_values_cents[current_coin_index]
            max_count = (amount_cents - current_amount) // coin  # Maximum count of the current coin

            # Try adding different counts of the current coin to explore possibilities
            for count in range(max_count + 1):
                new_amount = current_amount + count * coin
                new_combination = current_combination + [coins[current_coin_index]] * count
                # Push the new state onto the stack for further exploration
                stack.append((new_amount, new_combination, current_coin_index + 1))
    
    return best_solution

# Define the list of available coin denominations and the amount amount of change
L = [5, 2, 1, 0.5, 0.2, 0.1, 0.05]
A = 12.35

start = time.perf_counter()
solution = calculate_change_combinations(L, A)

with open("sol_4-6.txt", "w") as f:
    f.write(str(solution))
    f.write("\n")

total_time_3 = time.perf_counter() - start

start = time.perf_counter()
solution = calculate_change_combinations(L, A)
total_time_6 = time.perf_counter() - start

print("Solution: ", solution)
print("Total time for program 3: ", total_time_3)
print("Total time for program 6: ", total_time_6)




