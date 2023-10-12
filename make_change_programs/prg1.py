# gm
import time

# Greedy : function to make change with sorted coins
def greedy_make_change(amount, coins):
    i = 0
    change = []

    while amount > 0 and len(coins) > i:
        # print(str(round(amount//coins[i])) + " Coins of " + str(coins[i]) + "€")
        for j in range(round(amount//coins[i])):
            change.append(coins[i])
        amount = round(amount%coins[i], 2)
        i = i+1
    if amount > 0:
        print(f"Cannot make exact change for {amount:.2f}€")
    return change


# Initialisation
L = [5,2,1,0.5,0.2,0.1,0.05]
A = 12.35

start_time = time.perf_counter()
solution = greedy_make_change(A, L)
total_time = time.perf_counter() - start_time

# Print to file
with open("sol_1.txt", "w") as f:
    f.write(str(solution))
    f.write("\n")
    f.write(str(total_time))

