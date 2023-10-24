# Import the unittest module for writing unit tests
import unittest
# Import the TicTacToe class from the specified module
from homework_2_pyscaffold_bparento.ticTacToe import TicTacToe, ai_make_move

class TestTicTacToeAI(unittest.TestCase):
    def test_make_move_valid(self):
        game = TicTacToe()
        self.assertTrue(game.make_move(0))

    def test_make_move_invalid(self):
        game = TicTacToe()
        game.make_move(0)
        self.assertFalse(game.make_move(0))

    def test_switch_player(self):
        game = TicTacToe()
        game.switch_player()
        self.assertEqual(game.current_player, "O")
        game.switch_player()
        self.assertEqual(game.current_player, "X")

    def test_check_winner_draw(self):
        game = TicTacToe()
        game.board = ["X", "O", "X", "X", "O", "X", "O", "X", "O"]
        self.assertEqual(game.check_winner(), "Draw")

    def test_check_winner_horizontal(self):
        game = TicTacToe()
        game.board = ["X", "X", "X", "O", "O", " ", "O", "X", "X"]
        self.assertEqual(game.check_winner(), "X")

    def test_ai_make_move(self):
        game = TicTacToe()
        ai_make_move(game)  # Ensure the AI can make a move without errors
        self.assertIsNotNone(game.check_winner())
    
    def test_switch_player_start_with_X(self):
        game = TicTacToe()  # Create a new game, which starts with "X"
        self.assertEqual(game.current_player, "X")

    def test_switch_player_after_switching(self):
        game = TicTacToe()
        initial_player = game.current_player
        game.switch_player()  # Switch to the other player
        self.assertNotEqual(initial_player, game.current_player)
        self.assertEqual(game.current_player, "O") if initial_player == "X" else "X"

if __name__ == "__main__":
    unittest.main()
