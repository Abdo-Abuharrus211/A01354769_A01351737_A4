from unittest import TestCase
from unittest.mock import patch

from game_state_control import check_for_final_boss


class TestCheckForFinalBoss(TestCase):

    def test_check_for_final_boss_exception_raised(self):
        char_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 20}
        with self.assertRaises(KeyError):
            check_for_final_boss(char_test)

    @patch('random.randint', return_value=1)
    def test_check_for_final_boss_fail_low_level_no_chance(self, _):
        char_one = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 20,
                    "Knowledge": "Novice"}
        self.assertFalse(check_for_final_boss(char_one))

    @patch('random.randint', return_value=6)
    def test_check_for_final_boss_fail_low_level_has_chance(self, _):
        char_two = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 206,
                    "Knowledge": "Bookworm"}
        self.assertFalse(check_for_final_boss(char_two))

    @patch('random.randint', return_value=1)
    def test_check_for_final_boss_fail_high_level_no_chance(self, _):
        char_three = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 302,
                      "Knowledge": "Master Custodian"}
        self.assertFalse(check_for_final_boss(char_three))

    @patch('random.randint', return_value=7)
    def test_check_for_final_boss_pass(self, _):
        char_four = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 310,
                     "Knowledge": "Master Custodian"}
        self.assertTrue(check_for_final_boss(char_four))
