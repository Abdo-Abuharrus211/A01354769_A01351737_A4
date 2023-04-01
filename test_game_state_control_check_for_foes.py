
from unittest import TestCase
from unittest.mock import patch

from game_state_control import check_for_foes


class TestTestForFoes(TestCase):

    @patch('random.randint', return_value=2)
    def test_check_for_foes_none(self, _):
        check_for_foes()
        expected_output = True
        self.assertEqual(expected_output, check_for_foes())

    @patch('random.randint', return_value=4)
    def test_check_for_foes_present(self, _):
        check_for_foes()
        expected_output = False
        self.assertEqual(expected_output, check_for_foes())
