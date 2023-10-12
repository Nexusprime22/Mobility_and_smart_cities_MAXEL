# aw
import time

# Function to count occurrences of items in a list
def count_occurrences(array):
    counts = {}
    for item in array:
        if item in counts:
            counts[item] += 1  # If the item is already in the dictionary, increment its count
        else:
            counts[item] = 1  # If the item is not in the dictionary, add it with a count of 1
    return counts

# Function to calculate all combinations of coins to make a specific amount
def calculate_change_combinations(coins, amount):
    # Convert euro amounts to cents for calculations
    amount_cents = int(amount * 100)
    coin_values_cents = [int(coin * 100) for coin in coins]

    # Initialize a list to store combinations and their counts
    combinations = []
    stack = [(0, [], 0)]  # (current amount in cents, current combination, current coin index)

    while stack:
        current_amount, current_combination, current_coin_index = stack.pop()

        # If the current combination sums up to the target amount, add it to the list
        if current_amount == amount_cents:
            combinations.append(current_combination)
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

    # Print the total number of combinations
    print(f"Total number of combinations: {len(combinations)}")
    return combinations

# Define the list of available coin denominations and the amount amount of change
coin_list = [5, 2, 1, 0.5, 0.2, 0.1, 0.05]
print("The types of coins we have are:", coin_list)
change_amount = 12.35
print("The amount of change we need to return is:", change_amount)

start_time = time.perf_counter()
# Call the function to calculate and display the combinations of coins for the given amount
combinations = calculate_change_combinations(coin_list, change_amount)
total_time = time.perf_counter() - start_time

# Write the solution to a .txt file
with open("sol_2.txt", "w") as f:
    f.write(str(combinations))
    f.write("\n\n")
    f.write("Execution time is: " + str(total_time))