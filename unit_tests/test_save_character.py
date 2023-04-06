import os
import json
import pathlib
import unittest
from unittest.mock import patch

from Progression_and_Save_files.reload_character import save_character


class TestSaveCharacter(unittest.TestCase):
    def test_save_character_file_exist(self):
        self.assertTrue(os.path.exists('../Progression_and_Save_files/saved_character.json'))

    def test_save_character(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 30, "Current XP": 0, "Knowledge": "Novice"}
        save_character(character)
        with open('../Progression_and_Save_files/saved_character.json', 'r') as file:
            saved_character = json.load(file)
            self.assertEqual(character, saved_character)

    @patch('builtins.input', return_value='N')
    def test_save_character_no(self, _):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 30, "Current XP": 0, "Knowledge": "Novice"}
        with _:
            self.assertFalse(save_character(character))

    @patch('builtins.input', side_effect=['Y', 'N'])
    def test_save_character_invalid_input(self, _):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 30, "Current XP": 0, "Knowledge": "Novice"}
        with _:
            self.assertTrue(save_character(character))
