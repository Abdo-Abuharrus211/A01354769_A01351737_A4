from game_state_control import level_up
from unittest import TestCase


class TestLevelUp(TestCase):

    def test_level_up_yes(self):
        character_test = {"Current XP": 360, "Knowledge": 1}
        self.assertEqual(True, level_up(character_test))