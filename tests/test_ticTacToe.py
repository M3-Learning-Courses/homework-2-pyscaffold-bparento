# Import the unittest module for writing unit tests
import unittest
# Import the TicTacToe class from the specified module
from homework_2_pyscaffold_bparento.ticTacToe import TicTacToe

# Create a test case class that inherits from unittest.TestCase
class TestTicTacToe(unittest.TestCase):
    
    # Method to set up the game before each test
    def setUp(self):
        self.game = TicTacToe()

    # Test for the make_move method
    def test_make_move(self):
        # Check if the game correctly allows the first move (0)
        self.assertTrue(self.game.make_move(0))
        # Check if the game correctly disallows a move to an occupied position (0)
        self.assertFalse(self.game.make_move(0))
        # Check if the game correctly allows the next move (1)
        self.assertTrue(self.game.make_move(1))

    # Test for the switch_player method
    def test_switch_player(self):
        # Check if the current player is initially "X"
        self.assertEqual(self.game.current_player, "X")
        # Switch the player and verify if it's now "O"
        self.game.switch_player()
        self.assertEqual(self.game.current_player, "O")
        # Switch the player again and verify if it's back to "X"
        self.game.switch_player()
        self.assertEqual(self.game.current_player, "X")

    # Test for checking a draw scenario
    def test_check_winner_draw(self):
        # Set up the game board with a draw scenario
        self.game.board = ["X", "O", "X", "X", "X", "O", "O", "X", "O"]
        # Check if the game correctly identifies a draw
        self.assertEqual(self.game.check_winner(), "Draw")

    # Test for checking a horizontal win scenario
    def test_check_winner_horizontal(self):
        # Set up the game board with a horizontal win for "X"
        self.game.board = ["X", "X", "X", "O", "O", " ", "O", "X", "X"]
        # Check if the game correctly identifies "X" as the winner
        self.assertEqual(self.game.check_winner(), "X")

    # Test for checking a vertical win scenario
    def test_check_winner_vertical(self):
        # Set up the game board with a vertical win for "X"
        self.game.board = ["X", "O", "X", "X", "O", "X", "O", "X", "O"]
        # Check if the game correctly identifies "X" as the winner
        self.assertEqual(self.game.check_winner(), "X")

    # Test for checking a diagonal win scenario
    def test_check_winner_diagonal(self):
        # Set up the game board with a diagonal win for "X"
        self.game.board = ["X", "O", "O", "O", "X", "O", "O", "O", "X"]
        # Check if the game correctly identifies "X" as the winner
        self.assertEqual(self.game.check_winner(), "X")

    # Test for checking a scenario with no winner
    def test_check_winner_no_winner(self):
        # Set up the game board with no clear winner
        self.game.board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        # Check if the game correctly identifies that there is no winner
        self.assertIsNone(self.game.check_winner())

# Entry point for running the unit tests when the script is executed
if __name__ == "__main__":
    unittest.main()
