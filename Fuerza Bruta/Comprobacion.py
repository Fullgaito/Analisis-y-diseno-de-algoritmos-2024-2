import itertools
import time

def brute_force_eight_queens():
    """Solve the eight queens problem using brute force."""
    n = 8
    solutions = []
    total_checked = 0

    # Generate all permutations of 8 positions (0 to 7)
    for perm in itertools.permutations(range(n)):
        total_checked += 1
        # Check if the permutation satisfies the diagonal constraints
        if all(abs(perm[i] - perm[j]) != abs(i - j) for i in range(n) for j in range(i + 1, n)):
            solutions.append(perm)

    return solutions, total_checked

def backtracking_eight_queens():
    """Solve the eight queens problem using backtracking."""
    n = 8
    solutions = []
    total_checked = 0

    def is_valid(board, row, col):
        # Check if placing a queen at (row, col) is valid
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(row, board):
        nonlocal total_checked
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            total_checked += 1
            if is_valid(board, row, col):
                board[row] = col
                solve(row + 1, board)
                board[row] = -1

    solve(0, [-1] * n)
    return solutions, total_checked

# Measure time and run brute force
start_time = time.time()
brute_force_solutions, brute_force_checked = brute_force_eight_queens()
brute_force_time = time.time() - start_time

# Measure time and run backtracking
start_time = time.time()
backtracking_solutions, backtracking_checked = backtracking_eight_queens()
backtracking_time = time.time() - start_time

# Print results
print("Brute Force:")
print(f"  Solutions Found: {len(brute_force_solutions)}")
print(f"  Configurations Checked: {brute_force_checked}")
print(f"  Time Taken: {brute_force_time:.6f} seconds")

print("\nBacktracking:")
print(f"  Solutions Found: {len(backtracking_solutions)}")
print(f"  Configurations Checked: {backtracking_checked}")
print(f"  Time Taken: {backtracking_time:.6f} seconds")
