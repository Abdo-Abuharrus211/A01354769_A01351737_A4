from unittest import TestCase

from game_state_control import validate_move


class TestValidateMove(TestCase):

    def test_validate_move_exception_raised(self):
        character_test = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 10}
        with self.assertRaises(KeyError):
            validate_move({(0, 0): "Potato", (0, 1): "Pie", (1, 0): "Cheese", (1, 1): "Burger"}, character_test, "N")
    def test_validate_move_south(self):
        self.assertEqual(True, validate_move({(0, 0): "Potato", (0, 1): "Pie", (1, 0): "Cheese", (1, 1): "Burger"},
        {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}, "S"))

    def test_validate_move_north(self):
        self.assertEqual(True, validate_move({(0, 0): "Potato", (0, 1): "Pie", (1, 0): "Cheese", (1, 1): "Burger"},
        {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}, "N"))

    def test_validate_move_east(self):
        self.assertEqual(True, validate_move({(0, 0): "Potato", (0, 1): "Pie", (1, 0): "Cheese", (1, 1): "Burger"},
        {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}, "E"))

    def test_validate_move_west(self):
        self.assertEqual(True, validate_move({(0, 0): "Potato", (0, 1): "Pie", (1, 0): "Cheese", (1, 1): "Burger"},
        {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}, "W"))

    def test_validate_move_key_error_E(self):
        with self.assertRaises(KeyError):
            test_board = {(0, 0): "Potato", (0, 1): "Pie", (1, 0): "Cheese", (1, 1): "Burger"}
            test_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
            test_direction = "E"
            validate_move(test_board, test_character, test_direction)

    def test_validate_move_key_error_W(self):
        with self.assertRaises(KeyError):
            test_board = {(0, 0): "Potato", (0, 1): "Pie", (1, 0): "Cheese", (1, 1): "Burger"}
            test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
            test_direction = "W"
            validate_move(test_board, test_character, test_direction)

    def test_validate_move_key_error_N(self):
        with self.assertRaises(KeyError):
            test_board = {(0, 0): "Potato", (0, 1): "Pie", (1, 0): "Cheese", (1, 1): "Burger"}
            test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
            test_direction = "N"
            validate_move(test_board, test_character, test_direction)

    def test_validate_move_key_error_S(self):
        with self.assertRaises(KeyError):
            test_board = {(0, 0): "Potato", (0, 1): "Pie", (1, 0): "Cheese", (1, 1): "Burger"}
            test_character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
            test_direction = "S"
            validate_move(test_board, test_character, test_direction)



