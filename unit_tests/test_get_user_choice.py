
from unittest import TestCase
from unittest.mock import patch

from game_user_io import get_user_choice


class TestGetUserBoard(TestCase):

    @patch('builtins.input', side_effect=["T"])
    def test_get_user_choice_value_error_letter(self, _):
        with self.assertRaises(ValueError):
            get_user_choice()

    @patch('builtins.input', side_effect=["1"])
    def test_get_user_choice_value_error_number(self, _):
        with self.assertRaises(ValueError):
            get_user_choice()

    @patch('builtins.input', side_effect=["W"])
    def test_get_user_choice_W(self, _):
        get_user_choice()
        expected_output = "W"
        self.assertEqual(expected_output, "W")

    @patch('builtins.input', side_effect=["N"])
    def test_get_user_choice_N(self, _):
        get_user_choice()
        expected_output = "N"
        self.assertEqual(expected_output, "N")

    @patch('builtins.input', side_effect=["S"])
    def test_get_user_choice_S(self, _):
        get_user_choice()
        expected_output = "S"
        self.assertEqual(expected_output, "S")

    @patch('builtins.input', side_effect=["E"])
    def test_get_user_choice_E(self, _):
        get_user_choice()
        expected_output = "E"
        self.assertEqual(expected_output, "E")


