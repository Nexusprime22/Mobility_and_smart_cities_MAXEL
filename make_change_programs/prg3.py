# km
import math
import time

def make_change_recursive(coins, amount, start, current_change, result):
    if amount == 0:
        result.append(current_change[:])
        return

    for i in range(start, len(coins)):
        coin_cents = round(coins[i] * 100)
        if amount >= coin_cents:
            current_change.append(coins[i])
            make_change_recursive(coins, amount - coin_cents, i, current_change, result)
            current_change.pop()

    return result

def main():
    coins = [5, 2, 0.2, 0.1, 0.05]  # Available coin values
    target_amount = 12.35  # Change to be made
    solutions = []  # Store all valid combinations

    start_time = time.perf_counter()
    solutions = make_change_recursive(coins, target_amount * 100, 0, [], [])
    end_time = time.perf_counter()

    duration = end_time - start_time

    with open("AllTheSolutionsTest1.txt", "w") as file:
        # file.write("execution time: "+str(duration)+"s\n")
        file.write(str(solutions))
        # for solution in solutions:
        #     file.write(",".join(map(str, solution)) + "\n")
        #     print(solution,"\n")

        file.write("\n"+str(duration)+"\n")
        print("execution time: "+str(duration)+"s")
if __name__ == "__main__":
    main()