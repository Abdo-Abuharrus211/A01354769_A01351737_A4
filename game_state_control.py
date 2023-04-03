"""
This module is for functions controlling and checking the game's and other crucial control statements.
"""
import random


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Validate chosen direction.
    This functions determines if moving in given direction is permitted and within the board's bounds.

    :param board: dictionary representing the game board's rooms, with (x,y) coordinates as keys and string values.
    :param character: dictionary representing player's character stats, current location and HP
    :param direction: a string specifying which direction the player wants to move towards
    :precondition: character and direction are not None type and direction is a non-empty string
    :postcondition: Correctly checks if direction is valid and if the move keeps player within bounds
    :return: True if moving in player's desired direction is still within bounds, return False otherwise
    :raises KeyError: if moving in a direction leads out of bounds

     >>> board_one = {(0, 0): "Potato", (0, 1): "Pie", (1, 0): "Cheese", (1, 1): "Burger"}
     >>> character_one = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
     >>> direction_one = "S"
     >>> validate_move(board_one, character_one, direction_one)
     True
     >>> board_two = {(0, 0): "Potato", (1, 0): "Pie"}
     >>> character_two = {"X-coordinate": 0 , "Y-coordinate": 0, "Current HP": 5}
     >>> direction_two = "E"
     >>> validate_move(board_two, character_two, direction_two)
     True
     >>> board_three = {(0, 0): "Potato", (0, 1): "Pie", (1, 0): "Cheese", (1, 1): "Burger"}
     >>> character_three = {"X-coordinate": 1 , "Y-coordinate": 1, "Current HP": 5}
     >>> direction_three = "N"
     >>> validate_move(board_three, character_three, direction_three)
     True
     """
    if direction == "N" and 0 <= character["Y-coordinate"] - 1:
        valid_move = True
    elif direction == "S" and character["Y-coordinate"] + 1 <= max(board)[1]:
        valid_move = True
    elif direction == "E" and character["X-coordinate"] + 1 <= max(board)[0]:
        valid_move = True
    elif direction == "W" and 0 <= character["X-coordinate"] - 1:
        valid_move = True
    else:
        raise KeyError("Ah! You cannot go that way! You mustn't leave the bookshop, little one. You're too vulnerable "
                       "to venture beyond the territory of books.")
    return valid_move


def check_for_foes() -> bool:
    """
    Determine if there is a chance of encountering  foe.

    This function Determines if there's a 30% chance to face and fight a foe to fight by generating a random integer.

    :postcondition: generates random integer in a specific range then check if it's equal or greater than 25%
    :return: True if there's a 30% or more chance of facing a foe, return False otherwise
    """
    return random.randint(1, 6) <= 2


def dead_yet(character: dict) -> dict:
    """
    Determine if the player's character is dead.

    :param character: dictionary representing player's character stats, current location and HP
    :precondition: character is valid dictionary containing character's stats and not None type
    :postcondition: checks if character's HP is zero (dead) or if they're alive
    :return: True if the character's is dead, return False otherwise
     >>> character_one = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
     >>> dead_yet(character_one)
     False
     >>> character_two = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 2}
     >>> dead_yet(character_two)
     False
     >>> character_three = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 0}
     >>> dead_yet(character_three)
     True
    """
    return character["Current HP"] == 0


def level_up(character: dict):
    """
    Increase the character's knowledge level if they reach the level up threshold.

    a function that increases the character knowledge level based on experience points

    :param character: dictionary representing player's character stats, current location,current HP,
                        current XP and Knowledge
    :precondition character: must be a dictionary of character attributes
                             containing string keys X-coordinate, Y-coordinate, current HP, current XP and Knowledge
    :postcondition: update Knowledge if appropriate based on current XP
    >>> bob={"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 10, "Knowledge": "Novice"}
    >>> level_up(bob)
    >>> print(bob)
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 7, 'Current XP': 10, 'Knowledge': 'Novice'}
    >>> ellie={"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 101, "Knowledge": "Novice"}
    >>> level_up(ellie)
    Well done, little one. You're now a Bookworm! Keep going!
    >>> sam={"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 289, "Knowledge": "Bookworm"}
    >>> level_up(sam)
    The pupil has become a master. You're a Master Custodian now! You're ready to ascend.
    """
    if 0 <= character["Current XP"] < 100:
        character["Knowledge"] = "Novice"
    elif 100 <= character["Current XP"] < 200:
        character["Knowledge"] = "Bookworm"
        print("Well done, little one. You're now a Bookworm! Keep going!")
    elif 200 <= character["Current XP"] < 300:
        character["Knowledge"] = "Master Custodian"
        print("The pupil has become a master. You're a Master Custodian now! You're ready to ascend.")


def check_for_final_boss(character: dict) -> bool:
    """
    Determine if there's a 20% chance to face and fight a foe to fight by generating a random integer.

    :postcondition: generates random integer in a specific range then check if it's equal or greater than 25%
    :return: True if there's a 20% or more chance of facing a foe, return False otherwise
    """
    random_chance = random.randint(1, 10) >= 4
    if character["Current XP"] >= 300 and random_chance:
        return True
    else:
        return False


def main():
    """
    Drive the program.
    """
    pass


if __name__ == "__main__":
    main()
