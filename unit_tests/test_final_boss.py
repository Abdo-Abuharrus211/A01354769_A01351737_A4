import io
from unittest import TestCase
from unittest.mock import patch

from user_io import final_boss


class TestGuessingGame(TestCase):

    @patch('builtins.input', side_effect=[2])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_boss_correct_print(self, mock_output, _):
        character = {"Current HP": 5}
        final_boss(character)
        game_prints_this = mock_output.getvalue()
        expected_output = "Congratulations, you won!\n"
        self.assertEqual(expected_output, game_prints_this)

    @patch('builtins.input', side_effect=[3])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_boss_incorrect_print(self, mock_output, _):
        character = {"Current HP": 5}
        final_boss(character)
        game_prints_this = mock_output.getvalue()
        expected_output = "Incorrect, Caraxes has constricted the light out of you...I'm sorry little one\n"
        self.assertEqual(expected_output, game_prints_this)

    @patch('builtins.input', side_effect=[9])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_boss_out_of_range_print(self, mock_output, _):
        character = {"Current HP": 5}
        final_boss(character)
        game_prints_this = mock_output.getvalue()
        expected_output = "You did not chose an answer in range, game over\n"
        self.assertEqual(expected_output, game_prints_this)

    @patch('builtins.input', side_effect=["kate"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_out_non_number_print(self, mock_output, _,):
        character = {"Current HP": 5}
        final_boss(character)
        game_prints_this = mock_output.getvalue()
        expected_output = "You did not chose an answer in range, game over\n"
        self.assertEqual(expected_output, game_prints_this)

    @patch('builtins.input', side_effect=[3])
    def test_final_boss_incorrect_print_health(self, _):
        character = {"Current HP": 5}
        final_boss(character)
        expected_output = {"Current HP": 0}
        actual_output = character
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=["chris"])
    def test_final_boss_non_number_health(self, _):
        character = {"Current HP": 5}
        final_boss(character)
        expected_output = {"Current HP": 0}
        actual_output = character
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=[9])
    def test_final_boss_number_out_of_range_health(self, _):
        character = {"Current HP": 5}
        final_boss(character)
        expected_output = {"Current HP": 0}
        actual_output = character
        self.assertEqual(expected_output, actual_output)




