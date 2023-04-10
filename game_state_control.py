"""
This module is for functions controlling and checking the game's and other crucial control statements.
"""
import random

from dialog import LEVEL_TWO_REVELATION, SPACER


def validate_move(board: dict, character: dict, direction: str) -> bool:
    """
    Validate chosen direction.

    This functions determines if moving in given direction is permitted and within the board's bounds.

    :param board: dictionary representing the game board's rooms, with (x,y) coordinates as keys and string values.
    :param character: dictionary of representing the character and their attributes including X-Coordinate, Y-Coordinate
            Current HP, Current XP, &  Knowledge
    :param direction: a string specifying which direction the player wants to move towards
    :precondition character: must be dictionary of representing the character and their attributes with string
       keys: X-Coordinate, Y-Coordinate, Current HP, Current XP, &  Knowledge
    :precondition character: all dictionary values must be integers except for the one associated with "Knowledge"
               which must be a string either "Novice", "Bookworm" or "Master Custodian"
    :precondition direction: must be string either "W", "N", "S", or "W"
    :postcondition: Correctly checks if direction is valid and if the move keeps player within bounds
    :return: True if moving in player's desired direction is still within bounds, False otherwise
    :raise: KeyError if the character is missing a required attribute
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
    stat_list = ['X-coordinate', 'Y-coordinate']
    for attribute in stat_list:
        if attribute not in list(character.keys()):
            raise KeyError("Character Attribute not found")

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
    Check for foes.

    This function determines if the character will face and fight by generating a random integer.

    :postcondition: generates random integer in range 1 to 6 and checks if that number is less than or equal to 2
    :return: True if a foe is encountered (1/3 of the time), return False otherwise
    """
    return random.randint(1, 6) <= 2


def dead_yet(character: dict) -> dict:
    """
    Determine if the player's character is dead.

    :param character: dictionary of representing the character and their attributes including X-Coordinate, Y-Coordinate
            Current HP, Current XP, &  Knowledge
   :precondition board: must be a dictionary with a tuple of integers representing coordinates as keys
    :precondition character: must be dictionary of representing the character and their attributes with string
                            keys: X-Coordinate, Y-Coordinate, Current HP, Current XP, &  Knowledge
    :precondition character: all dictionary values must be integers except for the one associated with "Knowledge"
                             which must be a string either "Novice", "Bookworm" or "Master Custodian"
    :postcondition: checks if character's HP is zero (dead) or if they're alive
    :return: True if the character's is dead, return False otherwise
    :raise: KeyError if the character is missing a required attribute
     >>> character_one = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 10, "Knowledge": "Novice"}
     >>> dead_yet(character_one)
     False
     >>> character_two = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 1, "Current XP": 10, "Knowledge": "Novice"}
     >>> dead_yet(character_two)
     False
     >>> character_three = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 0, "Current XP": 10, "Knowledge": "Novice"}
     >>> dead_yet(character_three)
     True
    """
    stat_list = ['X-coordinate', 'Y-coordinate', 'Current HP', 'Current XP', 'Knowledge']
    for attribute in stat_list:
        if attribute not in list(character.keys()):
            raise KeyError("Character Attribute not found")

    return character["Current HP"] == 0


def damage_received(character):
    """
    Adjust damage received.

    This function adjusts the amount of damage inflicted when attacked to mirror character resistance gains

    :param character: dictionary of representing the character and their attributes including X-Coordinate, Y-Coordinate
            Current HP, Current XP, &  Knowledge
    :precondition character: must be dictionary of representing the character and their attributes with string
                            keys: X-Coordinate, Y-Coordinate, Current HP, Current XP, &  Knowledge
    :precondition character: all dictionary values must be integers except for the one associated with "Knowledge"
                         which must be a string either "Novice", "Bookworm" or "Master Custodian"
    :return: the appropriate amount of damage inflicted as in integer
    :raises KeyError: if the character is missing an attribute
    >>> bob = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 10, "Knowledge": "Novice"}
    >>> damage_received(bob)
    10
    >>> chad = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 111, "Knowledge": "Bookworm"}
    >>> damage_received(chad)
    5
    """
    stat_list = ['X-coordinate', 'Y-coordinate', 'Current HP', 'Current XP', 'Knowledge']
    for attribute in stat_list:
        if attribute not in list(character.keys()):
            raise KeyError("Character Attribute not found")

    if character["Knowledge"] == "Master Custodian":
        damage_inflicted = 3
    elif character["Knowledge"] == "Bookworm":
        damage_inflicted = 5
    else:
        damage_inflicted = 10
    return damage_inflicted


def level_up(character: dict):
    """
    Increase the character's level.

    This function increases the character knowledge level if they have the threashhold number of experience points

    :param character: dictionary representing player's character stats, current location,current HP,
                        current XP and Knowledge
    :precondition character: must be dictionary of representing the character and their attributes with string
                            keys: X-Coordinate, Y-Coordinate, Current HP, Current XP, &  Knowledge
    :precondition character: all dictionary values must be integers except for the one associated with "Knowledge"
                            which must be a string either "Novice", "Bookworm" or "Master Custodian"
    :postcondition: update Knowledge if appropriate based on current XP
    :postocondition: print appropriate congratulatory message
    :raise: KeyError if the character is missing an attribute
    >>> bob={"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 10, "Knowledge": "Novice"}
    >>> level_up(bob)
    >>> print(bob)
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 7, 'Current XP': 10, 'Knowledge': 'Novice'}
    >>> ellie={"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 101, "Knowledge": "Novice"}
    >>> level_up(ellie)
    Congratulations, young bookworm. Your tireless pursuit of knowledge has earned you the title
     of a true master of the written word. May your wisdom guide you further in your journey.
    ===========================================================
    >>> sam={"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 289, "Knowledge": "Bookworm"}
    >>> level_up(sam)
    The pupil has become a master. You're a Master Custodian now! You're ready to ascend.
    ===========================================================
    """
    stat_list = ['X-coordinate', 'Y-coordinate', 'Current HP', 'Current XP', 'Knowledge']
    for attribute in stat_list:
        if attribute not in list(character.keys()):
            raise KeyError("Character Attribute not found")

    if 0 <= character["Current XP"] < 100:
        character["Knowledge"] = "Novice"
    elif 100 <= character["Current XP"] < 200:
        character["Knowledge"] = "Bookworm"
        print(LEVEL_TWO_REVELATION)
        print(SPACER)
    elif 200 <= character["Current XP"] < 300:
        character["Knowledge"] = "Master Custodian"
        print(f"The pupil has become a master. You're a Master Custodian now! You're ready to ascend.")
        print(SPACER)


def check_for_final_boss(character: dict) -> bool:
    """
    Checks for final boss.

    This fumnction determines if the player is ready to face the Final Boss based on XP points
    and, if so, generate final boss 40% of the time

    :param character: dictionary of representing the character and their attributes including X-Coordinate, Y-Coordinate
            Current HP, Current XP, &  Knowledge
    :precondition character: must be dictionary of representing the character and their attributes with string
                            keys: X-Coordinate, Y-Coordinate, Current HP, Current XP, &  Knowledge
    :precondition character: all dictionary values must be integers except for the one associated with "Knowledge"
                            which must be a string either "Novice", "Bookworm" or "Master Custodian"
    :postcondition: generates random integer in a specific range then check if it's equal or greater than 25%
    :return: True if the character will face the final boss (40% of the time) when player's ready,
                return False otherwise
    :raise: KeyError if the character is missing an attribute
    """
    stat_list = ['X-coordinate', 'Y-coordinate', 'Current HP', 'Current XP', 'Knowledge']
    for attribute in stat_list:
        if attribute not in list(character.keys()):
            raise KeyError("Character Attribute not found")

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
