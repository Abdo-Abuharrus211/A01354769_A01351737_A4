from game_state_control import level_up
from unittest import TestCase


class TestLevelUp(TestCase):

    def test_level_up_yes(self):
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 10, "Current XP": 120, "Knowledge": 1}
        level_up(character_test)
        expected_level_up = 2
        self.assertEqual(expected_level_up, character_test["Knowledge"])
