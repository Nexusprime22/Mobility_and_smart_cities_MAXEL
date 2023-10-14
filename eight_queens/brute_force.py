def is_safe(board, row, col):
    # check if safe to place a queen at board[row][col]
    for i in range(col):
        if board[row][i] == 1:
            return False
        if row - i >= 0 and board[row - i][col - i] == 1:
            return False
        if row + i < len(board) and board[row + i][col - i] == 1:
            return False
    return True

def solve_queens(board, col):
    if col == len(board):
        # queens placed, and board valid
        print_board(board)
        return True
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_queens(board, col + 1):
                return True
            board[i][col] = 0
    return False

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "*" for cell in row))


board = [[0 for _ in range(8)] for _ in range(8)]
solve_queens(board, 0)