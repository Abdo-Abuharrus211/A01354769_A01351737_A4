import random


# def move_character(character: dict, direction: str) -> None:
#     """
#     Update character's location.
#
#     This function updates the character's location on the board.
#
#     :param character: dictionary of character attributes containing string keys X-coordinate, Y-coordinate and
#     current HP with integer values
#     :param character: dictionary of chara
#     :param direction: string of either 1 , 2 , 3 or 4
#     :precondition character: must be a dictionary of character attributes
#                              containing string keys X-coordinate, Y-coordinate and current HP
#     :precondition character: all dictionary values must be integers
#     :precondition direction: must be string of either 1 , 2 , 3 or 4
#     :postcondition: update the appropriate coordinate in character dictionary
#
#     >>> test_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
#     >>> move_character(test_character, "2")
#     >>> print(test_character)
#     {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
#
#     >>> test_character = {'X-coordinate': 2, 'Y-coordinate': 0, 'Current HP': 5}
#     >>> move_character(test_character, "3")
#     >>> print(test_character)
#     {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
#
#     """
#
#     if direction == "1":
#         character["Y-coordinate"] -= 1
#     elif direction == "2":
#         character["Y-coordinate"] += 1
#     elif direction == "3":
#         character["X-coordinate"] -= 1
#     elif direction == "4":
#         character["X-coordinate"] += 1


def guessing_game(character: dict):
    """
    Play a guessing game

    This function plays a guessing game where the player has to guess a randomly selected number between 1 and 5.

    :param character: dictionary of character attributes containing string keys X-coordinate, Y-coordinate and
                    current HP with integer values
    :precondition character: must be a dictionary of character attributes
                             containing string keys X-coordinate, Y-coordinate and current HP
    :precondition character: all dictionary values must be integers
    :postcondition: update to character dictionary if appropriate
    """

    # TODO: Kate's question guessing game, troubleshoot and fix together consulting Chris
    player_level = character["Level"]
    current_dictionary = (f"questions_level_{player_level:.0f}").format(player_level)
    question = random.choice(list(current_dictionary.items()))
    try:
        answer = int(input("Please input your answer as a number"))
    except ValueError:
        print("Please pick a number between 1 and 5 inclusive, you lost 1 HP")
        character["Current HP"] -= 1
    else:
        if answer < 1 or answer > 5:
            print("Please pick a number between 1 and 5 inclusive, you lost 1 HP")
            character["Current HP"] -= 1
        elif guess == current_dictionary[question]:
            print("You may pass unharmed")
        elif guess != secret_number:
            print("Incorrect, 1 hit taken")
            character["Current HP"] -= 1


def main():
    """
    Drive the program.
    """
    pass


if __name__ == "__main__":
    main()
