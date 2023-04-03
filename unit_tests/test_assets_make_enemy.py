
from unittest import TestCase
from unittest.mock import patch

from assets import make_enemy


class TestMakeEnemy(TestCase):

    @patch('random.randint', side_effect=[4])
    def test_make_enemy_4(self, _):
        actual_output = make_enemy()
        self.assertEqual(actual_output,  "A drunk flying moth is about to crash into us!")

    @patch('random.randint', side_effect=[15])
    def test_make_enemy_15(self, _):
        actual_output = make_enemy()
        self.assertEqual(actual_output, "Hold on that desk fan's gonna blow us awwaaaaaaaaaaaaaaaayyy")
