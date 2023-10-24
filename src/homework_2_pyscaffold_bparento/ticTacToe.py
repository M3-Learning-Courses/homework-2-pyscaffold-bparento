# class TicTacToe:
#     def __init__(self):
#         self.board = [" " for _ in range(9)]
#         self.current_player = "X"

#     def make_move(self, position):
#         if 0 <= position < 9 and self.board[position] == " ":
#             self.board[position] = self.current_player
#             return True
#         return False

#     def switch_player(self):
#         self.current_player = "X" if self.current_player == "O" else "O"

#     def check_winner(self):
#         win_conditions = [
#             [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
#             [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
#             [0, 4, 8], [2, 4, 6]  # Diagonals
#         ]

#         for condition in win_conditions:
#             a, b, c = condition
#             if self.board[a] == self.board[b] == self.board[c] != " ":
#                 return self.board[a]

#         if " " not in self.board:
#             return "Draw"

#         return None

#     def display_board(self):
#         # Function to display the current state of the game board
#         print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
#         print("---------")
#         print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
#         print("---------")
#         print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

# def play_game():
#     game = TicTacToe()
#     while True:
#         game.display_board()
#         position = int(input(f"Player {game.current_player}, enter your move (0-8): "))
#         if game.make_move(position):
#             winner = game.check_winner()
#             if winner:
#                 game.display_board()
#                 if winner == "Draw":
#                     print("It's a draw!")
#                 else:
#                     print(f"Player {winner} wins!")
#                 break
#             game.switch_player()

# if __name__ == "__main__":
#     play_game()

import random

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_player = random.choice(["X", "O"])  # Randomly choose who goes first

    def make_move(self, position):
        if 0 <= position < 9 and self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self):
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
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---------")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---------")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

def ai_make_move(game):
    # A simple AI strategy: Win if possible, block the opponent if they are about to win, or make a random move
    for position in range(9):
        if game.board[position] == " ":
            game.board[position] = game.current_player
            if game.check_winner() == game.current_player:
                return
            game.board[position] = " "

    for position in range(9):
        if game.board[position] == " ":
            game.board[position] = "X" if game.current_player == "O" else "O"
            if game.check_winner() == "X" or game.check_winner() == "O":
                game.board[position] = game.current_player
                return
            game.board[position] = " "

    while True:
        position = random.randint(0, 8)
        if game.make_move(position):
            return

def self_play_game():
    game = TicTacToe()
    while True:
        game.display_board()
        if game.current_player == "X":
            ai_make_move(game)
        else:
            while True:
                position = random.randint(0, 8)
                if game.make_move(position):
                    break

        winner = game.check_winner()
        if winner:
            game.display_board()
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"Player {winner} wins!")
            break

if __name__ == "__main__":
    self_play_game()
