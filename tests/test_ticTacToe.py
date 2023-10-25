# Import the unittest module for writing unit tests
import unittest
from unittest.mock import patch
import io

# Import the TicTacToe class from the specified module
from homework_2_pyscaffold_bparento.ticTacToe import TicTacToe, ai_make_move, self_play_game

class TestTicTacToe(unittest.TestCase):
    def test_initialization(self):
        """
        Test the initialization of the TicTacToe game.
        - Ensure the game board has 9 empty slots.
        - Verify that the starting player is either "X" or "O".
        """
        game = TicTacToe()
        self.assertEqual(len(game.board), 9)
        self.assertIn(game.current_player, ["X", "O"])

    def test_make_move_valid(self):
        """
        Test the make_move method with valid positions.
        - Ensure that moves are valid and return True.
        """
        game = TicTacToe()
        valid_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for position in valid_positions:
            self.assertTrue(game.make_move(position))

    def test_make_move_invalid(self):
        """
        Test the make_move method with invalid positions.
        - Ensure that moves to invalid positions return False.
        """
        game = TicTacToe()
        invalid_positions = [-1, 9, 10]
        for position in invalid_positions:
            self.assertFalse(game.make_move(position))

    def test_switch_player(self):
        """
        Test the switch_player method.
        - Verify that the current player switches from X to O and vice versa.
        """
        game = TicTacToe()
        initial_player = game.current_player
        game.switch_player()
        self.assertNotEqual(initial_player, game.current_player)

    def test_check_winner(self):
        """
        Test the check_winner method.
        - Set up a board with a winning condition and verify the winner is detected.
        """
        game = TicTacToe()
        game.board = ["X", "X", "X", " ", "O", "O", " ", " ", " "]
        self.assertEqual(game.check_winner(), "X")

    @patch('random.randint', side_effect=[1, 2, 3, 4, 5, 6, 7, 8, 0])
    def test_ai_make_move(self, mock_random):
        """
        Test the ai_make_move function.
        - Mock the random number generator to ensure specific moves.
        - Verify that the AI can win the game by placing three symbols in a row.
        """
        game = TicTacToe()
        game.current_player = "X"
        ai_make_move(game)
        self.assertIn(game.board, ["X", "X", "X", "X", "X", "X", "X", "X", "X"])

    def test_display_board(self):
        """
        Test the display_board method.
        - Capture the printed board and check if it contains the expected format.
        """
        game = TicTacToe()
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            game.display_board()
            output = mock_stdout.getvalue()
            self.assertTrue(" | " in output)
            self.assertTrue("---------" in output)
    
    @patch('random.randint', side_effect=[0, 1, 2, 3, 4, 5, 6, 7, 8])
    @patch('builtins.print')
    def test_self_play_game_draw(self, mock_print, mock_random):
        """
        Test the self_play_game function for a draw.
        - Mock the random number generator to simulate a draw.
        - Check if the game correctly ends in a draw.
        """
        self_play_game()
        mock_print.assert_called_with("It's a draw!")

    @patch('random.randint', side_effect=[0, 3, 1, 4, 2])
    @patch('builtins.print')
    def test_self_play_game_player_x_wins(self, mock_print, mock_random):
        """
        Test the self_play_game function for a win by Player X.
        - Mock the random number generator to simulate a win by Player X.
        - Verify that the function prints the correct winning message.
        """
        self_play_game()
        mock_print.assert_called_with("Player X wins!")

    @patch('random.randint', side_effect=[0, 3, 1, 4, 5])
    @patch('builtins.print')
    def test_self_play_game_player_o_wins(self, mock_print, mock_random):
        """
        Test the self_play_game function for a win by Player O.
        - Mock the random number generator to simulate a win by Player O.
        - Verify that the function prints the correct winning message.
        """
        self_play_game()
        mock_print.assert_called_with("Player O wins!")

if __name__ == '__main__':
    unittest.main()
