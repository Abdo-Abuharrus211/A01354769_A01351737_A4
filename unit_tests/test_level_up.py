from game_state_control import level_up
from unittest import TestCase


class TestLevelUp(TestCase):

    def test_level_up_no(self):
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 10, "Current XP": 70,
                          "Knowledge": "Novice"}
        level_up(character_test)
        expected_level_up = "Novice"
        self.assertEqual(expected_level_up, character_test["Knowledge"])

    def test_level_up_yes_bookworm(self):
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 10, "Current XP": 124,
                          "Knowledge": "Novice"}
        level_up(character_test)
        expected_level_up = "Bookworm"
        self.assertEqual(expected_level_up, character_test["Knowledge"])

    def test_level_up_yes_master_custodian(self):
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 10, "Current XP": 205,
                          "Knowledge": "Bookworm"}
        level_up(character_test)
        expected_level_up = "Master Custodian"
        self.assertEqual(expected_level_up, character_test["Knowledge"])
