from game_mechanics import move_character
from unittest import TestCase


class TestMoveCharacter(TestCase):

    def test_move_character_exception_raised(self):
        character_test = {"X-coordinate": 0, "Current HP": 10, "Current XP": 70, "Knowledge": "Novice"}
        with self.assertRaises(KeyError):
            move_character(character_test, "N")

    def test_move_character_S(self):
        character_location = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        move_character(character_location, "S")
        self.assertEqual({'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}, character_location)

    def test_move_character_N(self):
        character_location = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        move_character(character_location, "N")
        self.assertEqual({'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}, character_location)

    def test_move_character_E(self):
        character_location = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        move_character(character_location, "E")
        self.assertEqual({'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 5}, character_location)

    def test_move_character_W(self):
        character_location = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        move_character(character_location, "W")
        self.assertEqual({'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}, character_location)

    def test_move_character_not_allowed_letter(self):
        character_location = {"X-coordinate": 0, "Y-coordinate": 2, "Current HP": 5}
        move_character(character_location, "T")
        self.assertEqual({'X-coordinate': 0, 'Y-coordinate': 2, 'Current HP': 5}, character_location)

    def test_move_character_not_allowed_number(self):
        character_location = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        move_character(character_location, "6")
        self.assertEqual({'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}, character_location)

