import unittest
import json
import os
from unittest.mock import patch

from Progression_and_Save_files.reload_character import load_character


class TestLoadCharacter(unittest.TestCase):

    @patch('builtins.input', return_value='Y')
    def test_load_character(self, _):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 30, "Current XP": 0, "Knowledge": "Novice"}
        with open('../Progression_and_Save_files/saved_character.json', 'w') as file:
            json.dump(character, file)
        with _:
            loaded_character = load_character()
        self.assertDictEqual(character, loaded_character)

    @patch('builtins.input', return_value='Y')
    def test_load_character_no_file(self, _):
        with _:
            with self.assertRaises(FileNotFoundError):
                load_character()

    ...


if __name__ == '__main__':
    unittest.main()
