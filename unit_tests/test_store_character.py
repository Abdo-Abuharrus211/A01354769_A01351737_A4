import unittest
import pathlib
from unittest.mock import patch


class TestCase(unittest.TestCase):

    @patch('builtins.input', side_effect=["Y"])
    @patch('builtins.input', side_effect=["Y"])
    def test_store_character_file_exists(self):
        path = pathlib.Path("current_character.json")
        self.assertTrue(path.is_file())
