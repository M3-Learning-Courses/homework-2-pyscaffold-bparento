import random

class TicTacToe:
    def __init__(self):
        """
        Initialize a Tic-Tac-Toe game.
        - Initialize the game board with empty spaces.
        - Randomly choose the starting player (X or O).
        """
        self.board = [" " for _ in range(9)]
        self.current_player = random.choice(["X", "O"])

    def make_move(self, position):
        """
        Attempt to make a move on the game board.
        
        Parameters:
        - position (int): The position on the board where the current player wants to make a move.
        
        Returns:
        - True if the move is valid and successfully made, otherwise False.
        """
        if 0 <= position < 9 and self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self):
        """
        Switch the current player from X to O or from O to X.
        """
        self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self):
        """
        Check if there is a winner in the game.
        
        Returns:
        - The winning player (X or O) if there is a winner.
        - "Draw" if the game ended in a draw.
        - None if there is no winner yet.
        """
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for condition in win_conditions:
            a, b, c = condition
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]

        if " " not in self.board:
            return "Draw"

        return None

    def display_board(self):
        """
        Display the current state of the game board.
        """
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

def ai_make_move(game):
    """
    Implement a simple AI strategy: Win if possible, block the opponent if they are about to win, or make a random move.
    
    Parameters:
    - game (TicTacToe): The Tic-Tac-Toe game instance.
    """
    for position in range(9):
        if game.board[position] == " ":
            game.board[position] = game.current_player
            if game.check_winner() == game.current_player:
                return  # AI wins
            game.board[position] = " "  # Reset the move

    for position in range(9):
        if game.board[position] == " ":
            game.board[position] = "X" if game.current_player == "O" else "O"
            if game.check_winner() == "X" or game.check_winner() == "O":
                game.board[position] = game.current_player
                return  # Block the opponent
            game.board[position] = " "  # Reset the move

    while True:
        position = random.randint(0, 8)
        if game.make_move(position):
            return  # Make a random move

def self_play_game():
    """
    Play a self-playing Tic-Tac-Toe game using the AI strategy and random moves.
    """
    game = TicTacToe()
    while True:
        game.display_board()
        if game.current_player == "X":
            ai_make_move(game)  # AI's turn
        else:
            while True:
                position = random.randint(0, 8)
                if game.make_move(position):
                    break  # Random player's turn

        winner = game.check_winner()
        if winner:
            game.display_board()
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"Player {winner} wins!")
            break  # Game is over

if __name__ == "__main__":
    self_play_game()  # Start a self-playing game when the script is executed
