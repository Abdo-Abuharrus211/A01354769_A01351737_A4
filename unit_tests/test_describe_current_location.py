import io
from unittest import TestCase
from unittest.mock import patch

from A01354769_A01351737_A4.assets import make_board, make_character
from A01354769_A01351737_A4.game_mechanics import describe_current_location


class Test(TestCase):

    # Chris, you told us to let this go beyond character limit
    @patch('random.randint', side_effect=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location(self, mock_output, _):
        board = make_board(10, 10)
        character = make_character()
        describe_current_location(board, character)
        function_output = mock_output.getvalue()
        expected = "The dusty scrolls of the stacks howled with an eerie silence"
        self.assertEqual(expected, function_output)

