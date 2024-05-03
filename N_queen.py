import random

def is_safe(board, row, col):
  """
  Checks if placing a queen at (row, col) is safe (no conflicts).
  """
  n = len(board)
  # Check for conflicts in the same column above
  for i in range(row):
    if board[i][col] == 1:
      return False
  # Check for conflicts in diagonals
  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False
  for i, j in zip(range(row, n), range(col, n)):
    if board[i][j] == 1:
      return False
  return True

def solve_nqueens_hill_climbing(n):
  """
  Solves the N-Queens problem using Hill Climbing.
  """
  board = [[0 for _ in range(n)] for _ in range(n)]
  # Randomly place queens
  for i in range(n):
    board[i][random.randint(0, n-1)] = 1

  while True:
    # Find a better configuration (if possible)
    can_improve = False
    for row in range(n):
      for col in range(n):
        if board[row][col] == 0:  # Check empty cells
          new_board = [[x for x in row] for row in board]
          new_board[row][col] = 1
          if sum(is_safe(new_board, i, j) for i in range(n) for j in range(n)) > sum(is_safe(board, i, j) for i in range(n) for j in range(n)):
            board = new_board
            can_improve = True
            break
      if can_improve:
        break

    if not can_improve:
      # No improvement found, solution found
      break

  # Print the solution
  for row in board:
    print(row)

# Example usage
n = 4
solve_nqueens_hill_climbing(n)
