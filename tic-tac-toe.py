#README: NOT MY WORK
#Copied from ChatGPT on 10/16/2023

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        '''
        This function prints the Tic-Tac-Toe board
        :param board: # The initialize 3x3 board
        '''
        print(" | ".join(row))  # Print each row with '|' separator
        print("-" * 9)  # Print a horizontal line


# Function to check if a player has won
def check_win(board, player):
    
    # Check rows and columns for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals for a win
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the game is a draw
def check_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Function to play the Tic-Tac-Toe game
def play_tic_tac_toe():
    '''
    This function plays the Tic-Tac-Toe game
    '''
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize an empty 3x3 board  using list comprehension
    player = 'X'  # Player 'X' starts

    while True:
        print_board(board)  # Print the current state of the board
        print(f"Player {player}'s turn")

        # Get the player's move (row and column)
        row, col = map(int, input("Enter row and column (e.g., 1 2): ").split())
        
        # Check for invalid moves
        if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != ' ':
            print("Invalid move. Try again.")
            continue

        # Update the board with the player's move
        board[row - 1][col - 1] = player

        # Check if the current player has won
        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        # Check for a draw (all cells are filled)
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the other player's turn
        player = 'O' if player == 'X' else 'X'

# Entry point of the program
if __name__ == "__main__":
    play_tic_tac_toe() # Start the game

