class TicTacToe:
    def __init__(self):
        # Initialize the game board with empty spaces and set the current player to "X"
        self.board = [" " for _ in range(9)]
        self.current_player = "X"

    def make_move(self, position):
        # Method for making a move in the game
        # Check if the specified position is valid (0-8) and if it's an empty space
        if 0 <= position < 9 and self.board[position] == " ":
            # Place the current player's symbol in the specified position
            self.board[position] = self.current_player
            return True  # Return True to indicate a successful move
        return False  # Return False to indicate an invalid move

    def switch_player(self):
        # Method for switching the current player from "X" to "O" or vice versa
        self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self):
        # Method for checking if there's a winner or a draw
        # Define the winning conditions for rows, columns, and diagonals
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for condition in win_conditions:
            a, b, c = condition
            # Check if the symbols in the winning condition are the same and not empty
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]  # Return the symbol of the winner

        # If no winner has been found and the board is full, return "Draw"
        if " " not in self.board:
            return "Draw"

        return None  # If there's no winner or draw, return None

# This is the end of the TicTacToe class definition.
