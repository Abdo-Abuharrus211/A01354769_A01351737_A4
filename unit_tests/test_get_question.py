from unittest import TestCase
import io
from unittest.mock import patch


from guessing_game import get_question


class Test(TestCase):
    @patch('random.choice', return_value="What is NOT presented as true in Breathe by James Nestor")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_check_for_foes_none(self, mock_output, _):
        test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 20,
                        "Knowledge": "Novice"}
        get_question(test_character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = "Test output"
        self.assertEqual(expected_output, the_game_printed_this)

#     @patch('sys.stdout', new_callable=io.StringIO)
#     def test_simple_game(self, mock_output, random_number_generator, mock_input):
#         simple_game()
#         the_game_printed_this = mock_output.getvalue()
#         expected_output = "You're right!\n"
#         self.assertEqual(expected_output, the_game_printed_this)
#
#
# class Test(TestCase):
#     def test_get_question_novice_level(self):
#         char_one = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 20,
#                     "Knowledge": "Novice"}
