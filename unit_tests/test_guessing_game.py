import io
from unittest import TestCase
from unittest.mock import patch

from guessing_game import guessing_game


class TestGuessingGame(TestCase):

    @patch('builtins.input', side_effect=["T"])
    def test_guessing_game_value_error_letter(self, _):
        with self.assertRaises(ValueError):
            character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
            guessing_game(character)

        @patch('builtins.input', side_effect=[2])
        @patch('guessing.game.get_question')
        @patch('sys.stdout', new_callable=io.StringIO)
        def test_guessing_game_correct_print(self, mock_output, _, __):
            character = {"Current HP": 4, "Knowledge": 2}

            guessing_game(character)
            expected_output = "You may pass unharmed\n"
            self.assertIn(expected_output, mock_output.getvalue())

    @patch('builtins.input', side_effect=[3])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_incorrect_print(self, mock_output, _, __):
        character = {"Current HP": 5}
        guessing_game(character)
        game_prints_this = mock_output.getvalue()
        expected_output = "Incorrect, 1 hit taken\n"
        self.assertEqual(expected_output, game_prints_this)

    @patch('builtins.input', side_effect=[9])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_out_of_range_print(self, mock_output, _, __):
        character = {"Current HP": 5}
        guessing_game(character)
        game_prints_this = mock_output.getvalue()
        expected_output = "Please pick a number between 1 and 5 inclusive, you lost 1 HP\n"
        self.assertEqual(expected_output, game_prints_this)

    @patch('builtins.input', side_effect=["kate"])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_out_non_number_print(self, mock_output, _, __):
        character = {"Current HP": 5}
        guessing_game(character)
        game_prints_this = mock_output.getvalue()
        expected_output = "Please pick a number between 1 and 5 inclusive, you lost 1 HP\n"
        self.assertEqual(expected_output, game_prints_this)

    @patch('builtins.input', side_effect=[2])
    @patch('random.randint', return_value=2)
    def test_guessing_game_correct_print_health(self, _, __):
        character = {"Current HP": 5}
        guessing_game(character)
        expected_output = {"Current HP": 5}
        actual_output = character
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=[2])
    @patch('random.randint', return_value=3)
    def test_guessing_game_incorrect_print_health(self, _, __):
        character = {"Current HP": 5}
        guessing_game(character)
        expected_output = {"Current HP": 4}
        actual_output = character
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=["kate"])
    @patch('random.randint', return_value=3)
    def test_guessing_game_non_number_health(self, _, __):
        character = {"Current HP": 5}
        guessing_game(character)
        expected_output = {"Current HP": 4}
        actual_output = character
        self.assertEqual(expected_output, actual_output)

    @patch('builtins.input', side_effect=[9])
    @patch('random.randint', return_value=3)
    def test_guessing_game_non_number_health(self, _, __):
        character = {"Current HP": 3}
        guessing_game(character)
        expected_output = {"Current HP": 2}
        actual_output = character
        self.assertEqual(expected_output, actual_output)
