# km

# modify program 3 so as to evaluate the cost of a solution
# according to the number of units of the values. Calculate the best
# solution according to this cost by displaying successive values that
# improve. Display the trace of this execution in a file
# CORRECT_SolutionsWhichImproveIncrementally.txt
# Calculate the number of solutions displayed, and the display economy,
# using the wc –l command. Calculate with the time, or date command,
# the execution time programs 3 and 5

# wc -l command ?

import math
import time

def make_change_recursive_prg3(coins, amount, start, current_change, result):
    if amount == 0:
        result.append(current_change[:])
        return

    for i in range(start, len(coins)):
        coin_cents = round(coins[i] * 100)
        if amount >= coin_cents:
            current_change.append(coins[i])
            make_change_recursive_prg3(coins, amount - coin_cents, i, current_change, result)
            current_change.pop()

    return result

def calculate_solution_cost(solution):
    # Calculate the cost of a solution as the sum of units of values
    cost = sum([round(coin * 100) for coin in solution])
    return cost

def make_change_recursive(coins, amount, start, current_change, result, best_cost):
    if amount == 0:
        current_cost = calculate_solution_cost(current_change)
        if current_cost < best_cost[0]:
            result.append(current_change[:])
            best_cost[0] = current_cost
        return

    for i in range(start, len(coins)):
        coin_cents = round(coins[i] * 100)
        if amount >= coin_cents:
            current_change.append(coins[i])
            make_change_recursive(coins, amount - coin_cents, i, current_change, result, best_cost)
            current_change.pop()

def main():
    coins = [5, 2, 0.2, 0.1, 0.05]  # Available coin values
    target_amount = 12.35  # Change to be made
    solutions = []  # Store all valid combinations
    best_cost = [float('inf')]  # Initialize with a very high cost

    start_time_prg3 = time.perf_counter()
    solutions = make_change_recursive_prg3(coins, target_amount * 100, 0, [], [])
    end_time_prg3 = time.perf_counter()
    duration_prg3 = end_time_prg3 - start_time_prg3

    solutions = []
    start_time = time.perf_counter()
    make_change_recursive(coins, target_amount * 100, 0, [], solutions, best_cost)
    end_time = time.perf_counter()

    duration = end_time - start_time

    with open("CORRECT_SolutionsWhichImproveIncrementally.txt", "w") as file:
        file.write(str(solutions))
        file.write("\nPrevious Program 3 execution time: " + str(duration_prg3))
        file.write("\nModified Program 3 execution time: " + str(duration))
        # for solution in solutions:
        #     file.write(",".join(map(str, solution)) + "\n")

    print("Previous Program 3 execution time: " + str(duration_prg3) + "\n")
    print("Modified Program 3 execution time: " + str(duration) + "\n")
    print("Total solutions displayed:", len(solutions))

if __name__ == "__main__":
    main()
