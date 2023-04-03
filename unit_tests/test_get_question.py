from unittest import TestCase

from user_io import get_question


class Test(TestCase):
    def test_get_question_novice_level(self):
        char_one = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Current XP": 20,
                    "Knowledge": "Novice"}
