from unittest import TestCase
from unittest.mock import patch

from Progression_and_Save_files.load_or_new_game import load_char_or_new


class TestLoadCharOrNew(TestCase):

    @patch("builtins.input", return_value="1")
    def test_load_char_or_new(self, _):
        returned_char = load_char_or_new()
        new_char = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 0, "Knowledge": "Novice"}
        self.assertEqual(new_char, returned_char)

    @patch("builtins.input", side_effect=["2", "Y"])
    def test_load_char_or_load_saved(self, _):
        returned_char = load_char_or_new()
        saved_char = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 30, "Current XP": 0, "Knowledge": "Novice"}
        self.assertEqual(saved_char, returned_char)
