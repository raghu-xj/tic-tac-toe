import math

# Constants for the game
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

# Check if the game is over
def check_winner(board):
    # Check rows, columns, and diagonals
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None

# Check if the board is full
def is_board_full(board):
    return all(cell != EMPTY for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return -1  # Player X wins
    elif winner == PLAYER_O:
        return 1  # Player O wins
    elif is_board_full(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    score = minimax(board, depth + 1, False)
                    board[row][col] = EMPTY
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    score = minimax(board, depth + 1, True)
                    board[row][col] = EMPTY
                    best_score = min(best_score, score)
        return best_score

# Get the best move for the AI
def get_best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_O
                score = minimax(board, 0, False)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

# Print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Main game loop
def main():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    current_player = PLAYER_X

    while True:
        print_board(board)

        if current_player == PLAYER_X:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] != EMPTY:
                print("Invalid move! Try again.")
                continue
        else:
            row, col = get_best_move(board)

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"{winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = PLAYER_X if current_player == PLAYER_O else PLAYER_O

if __name__ == "__main__":
    main()
