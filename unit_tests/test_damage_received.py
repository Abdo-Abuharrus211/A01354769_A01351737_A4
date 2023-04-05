from unittest import TestCase

from game_state_control import damage_received


class TestDamageReceived(TestCase):

    def test_damage_received_exception_raised(self):
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 10, "Current XP": 70}
        with self.assertRaises(KeyError):
            damage_received(character_test)

    def test_damage_received_novice(self):
        bob = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 50, "Knowledge": "Novice"}
        self.assertEqual(10, damage_received(bob))

    def test_damage_received_bookworm(self):
        ellie = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 165, "Knowledge": "Bookworm"}
        self.assertEqual(5, damage_received(ellie))

    def test_damage_received_master_custodian(self):
        chad = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 279,
                "Knowledge": "Master Custodian"}
        self.assertEqual(3, damage_received(chad))
