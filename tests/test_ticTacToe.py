import unittest
from homework_2_pyscaffold_bparento.ticTacToe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_make_move(self):
        self.assertTrue(self.game.make_move(0))
        self.assertFalse(self.game.make_move(0))
        self.assertTrue(self.game.make_move(1))

    def test_switch_player(self):
        self.assertEqual(self.game.current_player, "X")
        self.game.switch_player()
        self.assertEqual(self.game.current_player, "O")
        self.game.switch_player()
        self.assertEqual(self.game.current_player, "X")

    def test_check_winner_draw(self):
        self.game.board = ["X", "O", "X", "X", "X", "O", "O", "X", "O"]
        self.assertEqual(self.game.check_winner(), "Draw")

    def test_check_winner_horizontal(self):
        self.game.board = ["X", "X", "X", "O", "O", " ", "O", "X", "X"]
        self.assertEqual(self.game.check_winner(), "X")

    def test_check_winner_vertical(self):
        self.game.board = ["X", "O", "X", "X", "O", "X", "O", "X", "O"]
        self.assertEqual(self.game.check_winner(), "X")

    def test_check_winner_diagonal(self):
        self.game.board = ["X", "O", "O", "O", "X", "O", "O", "O", "X"]
        self.assertEqual(self.game.check_winner(), "X")

    def test_check_winner_no_winner(self):
        self.game.board = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        self.assertIsNone(self.game.check_winner())

if __name__ == "__main__":
    unittest.main()