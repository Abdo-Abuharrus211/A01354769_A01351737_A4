from game_mechanics import move_character
from unittest import TestCase


class TestMoveCharacter(TestCase):

    def test_move_character_1(self):
        character_location = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        move_character(character_location, "1")
        self.assertEqual({'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}, character_location)

    def test_move_character_2(self):
        character_location = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        move_character(character_location, "2")
        self.assertEqual({'X-coordinate': 1, 'Y-coordinate': 2, 'Current HP': 5}, character_location)

    def test_move_character_3(self):
        character_location = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        move_character(character_location, "3")
        self.assertEqual({'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}, character_location)

    def test_move_character_not_allowed(self):
        character_location = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        move_character(character_location, "6")
        self.assertEqual({'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}, character_location)

    def test_move_character_4(self):
        character_location = {"X-coordinate": 1, "Y-coordinate": 2, "Current HP": 5}
        move_character(character_location, "4")
        self.assertEqual({'X-coordinate': 2, 'Y-coordinate': 2, 'Current HP': 5}, character_location)

    def test_move_character_not_allowed_letter(self):
        character_location = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        move_character(character_location, "h")
        self.assertEqual({'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}, character_location)

