# Sudoku Solver using Backtracking

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

# Print the Sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

# Find an empty cell
def find_empty(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None

# Check whether a number can be placed
def is_valid(board, num, row, col):

    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

# Solve Sudoku using Backtracking
def solve(board):

    empty = find_empty(board)

    if empty is None:
        return True

    row, col = empty

    for num in range(1, 10):

        if is_valid(board, num, row, col):

            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0

    return False

# Main Program
print("Original Sudoku:\n")
print_board(board)

print("\nSolving...\n")

if solve(board):
    print("Solved Sudoku:\n")
    print_board(board)
else:
    print("No solution exists.")