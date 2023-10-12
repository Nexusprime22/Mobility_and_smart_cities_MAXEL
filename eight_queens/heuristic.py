import random
import math

def is_safe(board, row, col):
    # Check if it's safe to place a queen at board[row][col]
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def count_conflicts(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def simulated_annealing(board, max_temp, min_temp, cooling_rate):
    current_solution = list(board)
    current_conflicts = count_conflicts(current_solution)
    best_solution = list(board)
    best_conflicts = current_conflicts

    temperature = max_temp

    while temperature > min_temp:
        new_solution = list(current_solution)
        row, col = random.randint(0, len(board) - 1), random.randint(0, len(board) - 1)
        new_solution[col] = row
        new_conflicts = count_conflicts(new_solution)

        if new_conflicts == 0:
            return new_solution  # A solution with zero conflicts is found.

        delta_e = new_conflicts - current_conflicts

        if delta_e < 0 or random.random() < math.exp(-delta_e / temperature):
            current_solution, current_conflicts = new_solution, new_conflicts

        if current_conflicts < best_conflicts:
            best_solution, best_conflicts = current_solution, current_conflicts

        temperature *= cooling_rate

    return best_solution  # Return the best solution found

def print_board(board):
    for row in board:
        print(" ".join("Q" if col == row else "*" for col in range(len(board))))

def eight_queens_heuristic(size, max_temp, min_temp, cooling_rate):
    board = [random.randint(0, size - 1) for _ in range(size)]
    solution = simulated_annealing(board, max_temp, min_temp, cooling_rate)
    print_board(solution)

# Example usage
eight_queens_heuristic(size=8, max_temp=100, min_temp=0.001, cooling_rate=0.95)
