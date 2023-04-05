import unittest
import pathlib
from reload_character import store_character
class TestCase(unittest.TestCase):

    @patch('builtins.input', side_effect=["Y"])
    @patch('builtins.input', side_effect=["Y"])
    def test_store_character_file_exists(self):
        path = pathlib.Path("current_character.json")
        self.assertTrue(path.is_file())


