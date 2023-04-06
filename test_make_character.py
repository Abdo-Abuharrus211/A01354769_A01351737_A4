from unittest import TestCase

from assets import make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        expectd_char = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 0, "Knowledge": "Novice"}
        self.assertEqual(expectd_char, make_character())
