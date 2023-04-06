import io
from unittest import TestCase
from unittest.mock import patch

from guessing_game import guessing_game


class TestGuessingGame(TestCase):

    @patch('random.randint', return_value=2)
    @patch('random.choice', side_effect={"Which book is the shortest? "
                                         "\n 1: Animal Farm \n 2: 1984\n 3: Lord of the Flies \n"
                                         " 4: Clockwork Orange \n 5: "
                                         "Catch 22": 1})
    @patch('builtins.input', side_effect=[1])
    def test_guessing_game_correct_print_health(self, _, __, ___):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 30, "Current XP": 0, "Knowledge": "Novice"}
        guessing_game(character)
        expected_output = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 30, "Current XP": 20,
                           "Knowledge": "Novice"}
        actual_output = character
        self.assertEqual(expected_output, actual_output)

    # @patch('builtins.input', side_effect=["T"])
    # def test_guessing_game_value_error_letter(self, _):
    #     with self.assertRaises(ValueError):
    #         character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 50, "Current XP": 0, "Knowledge": "Novice"}
    #         guessing_game(character)
    #
    @patch('random.randint', return_value=2)
    @patch('random.choice', side_effect={"Which book is the shortest? "
                                         "\n 1: Animal Farm \n 2: 1984\n 3: Lord of the Flies \n"
                                         " 4: Clockwork Orange \n 5: "
                                         "Catch 22": 1})
    @patch('builtins.input', side_effect=[1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_correct_print(self, mock_output, _, __, ___):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 50, "Current XP": 0, "Knowledge": "Novice"}
        guessing_game(character)
        actual_output = mock_output.getvalue()
        expected_output = "An Orb Weaver has blocked the path with its sticky web. " \
                          "You must answer the question to persevere! \n" \
                          " Which book is the shortest? \n " \
                          "1: Animal Farm \n " \
                          "2: 1984\n " \
                          "3: Lord of the Flies \n " \
                          "4: Clockwork Orange \n " \
                          "5: Catch 22\n" \
                          "You may pass unharmed\n"
        self.assertEqual(expected_output, actual_output)

    @patch('random.randint', return_value=2)
    @patch('random.choice', side_effect={"Which book is the shortest? "
                                         "\n 1: Animal Farm \n 2: 1984\n 3: Lord of the Flies \n"
                                         " 4: Clockwork Orange \n 5: "
                                         "Catch 22": 1})
    @patch('builtins.input', side_effect=[5])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_incorrect_print(self, mock_output, _, __, ___):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 50, "Current XP": 0, "Knowledge": "Novice"}
        guessing_game(character)
        game_prints_this = mock_output.getvalue()
        expected_output = "An Orb Weaver has blocked the path with its sticky web. " \
                          "You must answer the question to persevere! \n" \
                          " Which book is the shortest? \n " \
                          "1: Animal Farm \n " \
                          "2: 1984\n " \
                          "3: Lord of the Flies \n " \
                          "4: Clockwork Orange \n " \
                          "5: Catch 22\n" \
                          "'Incorrect, 1 hit taken'\n"
        self.assertEqual(expected_output, game_prints_this)

    @patch('random.randint', return_value=2)
    @patch('random.choice', side_effect={"Which book is the shortest? "
                                         "\n 1: Animal Farm \n 2: 1984\n 3: Lord of the Flies \n"
                                         " 4: Clockwork Orange \n 5: "
                                         "Catch 22": 1})
    @patch('builtins.input', side_effect=[7])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_out_of_range_print(self, mock_output, _, __, ___):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 30, "Current XP": 0, "Knowledge": "Novice"}
        guessing_game(character)
        game_prints_this = mock_output.getvalue()
        expected_output = "An Orb Weaver has blocked the path with its sticky web. " \
                          "You must answer the question to persevere! \n" \
                          " Which book is the shortest? \n " \
                          "1: Animal Farm \n " \
                          "2: 1984\n " \
                          "3: Lord of the Flies \n " \
                          "4: Clockwork Orange \n " \
                          "5: Catch 22\n" \
                          "'You must pick a number between 1 and 5 inclusive, you lost 1 HP'\n"
        self.assertEqual(expected_output, game_prints_this)

    @patch('random.randint', return_value=2)
    @patch('random.choice', side_effect={"Which book is the shortest? "
                                         "\n 1: Animal Farm \n 2: 1984\n 3: Lord of the Flies \n"
                                         " 4: Clockwork Orange \n 5: "
                                         "Catch 22": 1})
    @patch('builtins.input', side_effect=["kate"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_out_non_number_print(self, mock_output, _, __, ___):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 50, "Current XP": 0, "Knowledge": "Novice"}
        guessing_game(character)
        game_prints_this = mock_output.getvalue()
        expected_output = "An Orb Weaver has blocked the path with its sticky web. " \
                          "You must answer the question to persevere! \n" \
                          " Which book is the shortest? \n " \
                          "1: Animal Farm \n " \
                          "2: 1984\n " \
                          "3: Lord of the Flies \n " \
                          "4: Clockwork Orange \n " \
                          "5: Catch 22\n" \
                          "'Please pick a number between 1 and 5 inclusive, you lost 1 HP'\n"
        self.assertEqual(expected_output, game_prints_this)

    @patch('random.randint', return_value=2)
    @patch('random.choice', side_effect={"Which book is the shortest? "
                                         "\n 1: Animal Farm \n 2: 1984\n 3: Lord of the Flies \n"
                                         " 4: Clockwork Orange \n 5: "
                                         "Catch 22": 1})
    @patch('builtins.input', side_effect=["kate"])
    def test_guessing_game_incorrect_print_health(self, _, __, ___):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 30, "Current XP": 0, "Knowledge": "Novice"}
        guessing_game(character)
        actual_output = character
        expected_output = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 20, "Current XP": 0,
                           "Knowledge": "Novice"}
        self.assertEqual(expected_output, actual_output)

    @patch('random.randint', return_value=2)
    @patch('random.choice', side_effect={"Which book is the shortest? "
                                         "\n 1: Animal Farm \n 2: 1984\n 3: Lord of the Flies \n"
                                         " 4: Clockwork Orange \n 5: "
                                         "Catch 22": 1})
    @patch('builtins.input', side_effect=["kate"])
    def test_guessing_game_non_number_health(self, _, __, ___):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 50, "Current XP": 0, "Knowledge": "Novice"}
        guessing_game(character)
        expected_output = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 40, "Current XP": 0,
                           "Knowledge": "Novice"}
        actual_output = character
        self.assertEqual(expected_output, actual_output)
