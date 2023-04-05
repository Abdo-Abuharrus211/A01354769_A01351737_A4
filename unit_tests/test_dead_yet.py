from game_state_control import dead_yet
from unittest import TestCase


class TestDeadYet(TestCase):

    def test_dead_yet_exception_raised(self):
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 10}
        with self.assertRaises(KeyError):
            dead_yet(character_test)

    def test_dead_yet_yes(self):
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 0, "Current XP": 10,
                          "Knowledge": "Novice"}
        self.assertEqual(True, dead_yet(character_test))

    def test_dead_yet_no(self):
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 10,
                          "Knowledge": "Novice"}
        self.assertEqual(False, dead_yet(character_test))
