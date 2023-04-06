import io
from unittest import TestCase
from unittest.mock import patch

from assets import make_board, make_character
from game_mechanics import describe_current_location


class Test(TestCase):

    def test_describe_current_location_character_exception_raised(self):
        character_test = {"X-coordinate": 0, "Current HP": 10, "Current XP": 70, "Knowledge": "Novice"}
        with self.assertRaises(KeyError):
            describe_current_location(make_board(10, 10), character_test)

    # TODO: Chris, you told us to let this go beyond character limit
    # TODO: Do I use 100 for 100 calls of randint or 24 for the tuple's length
    @patch('random.randint', side_effect=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
                                          22, 23])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location(self, mock_output, _):
        board = make_board(10, 10)
        character = make_character()
        describe_current_location(board, character)
        function_output = mock_output.getvalue()
        expected = "The dusty scrolls of the stacks howled with an eerie silence"
        self.assertEqual(expected, function_output)
