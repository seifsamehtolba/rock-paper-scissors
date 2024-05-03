import unittest
from unittest.mock import patch
from io import StringIO
import rps_game  # assuming your game code is in rps_game.py

class TestRockPaperScissorsGame(unittest.TestCase):
    def test_determine_winner_player_wins(self):
        with patch('builtins.input', side_effect=['R']), \
             patch('sys.stdout', new=StringIO()) as fake_out:
            rps_game.main()
            output = fake_out.getvalue().strip()
            self.assertIn("You win!", output)

    def test_determine_winner_computer_wins(self):
        with patch('builtins.input', side_effect=['S']), \
             patch('sys.stdout', new=StringIO()) as fake_out:
            rps_game.main()
            output = fake_out.getvalue().strip()
            self.assertIn("Computer wins!", output)

    def test_determine_winner_draw(self):
        with patch('builtins.input', side_effect=['P']), \
             patch('sys.stdout', new=StringIO()) as fake_out:
            rps_game.main()
            output = fake_out.getvalue().strip()
            self.assertIn("It's a draw!", output)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
