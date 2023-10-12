# gm

# You calculate all the solutions that you do not display, as you go.
# If you store the solutions in a 2D array of solutions, in the order in which
# the valid combinations are found, then a subsequent display following
# that order can be compared with the contents of the CORRECT_ ... file
# and will show no difference.

import time

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
    
    return combinations

# Define the list of available coin denominations and the amount amount of change
L = [5, 2, 1, 0.5, 0.2, 0.1, 0.05]
A = 12.35

start = time.perf_counter()
solution = calculate_change_combinations(L, A)
total_time = time.perf_counter() - start

with open("sol_4.txt", "w") as f:
    f.write(str(solution))
    f.write("\n")
    f.write(str(total_time))


# Read CORRECT_ ... file and compare with the contents of the list of solutions
    # Do not consider the last line
with open("AllTheSolutionsTest1.txt", "r") as f:
    correct_solution = f.read().splitlines()[:-1]


# Sort each array on correct_solution and solution
for i in range(len(solution)):
    solution[i].sort()

for i in range(len(correct_solution)):
    correct_solution[i] = correct_solution[i].replace("[", "").replace("]", "").replace(",", "").split()
    correct_solution[i].sort()

# Check if each element of correct_solution is in solution
missing = 0
missing_solution = []
for i in range(len(correct_solution)):
    if correct_solution[i] not in solution:
        print("ERROR: solution not found")
        missing +=1
        missing_solution.append(correct_solution[i])

print("Number of missing solutions: ", missing)
# print("Missing solutions: ", missing_solution)