"""
    This module is for functions that comprise the game's core elements and mechanics.
"""


def describe_current_location(board: dict, character: dict):
    """
    Describe the room the player is currently in.

    :param board: dictionary representing the game board's rooms, with (x,y) coordinates as keys and string values.
    :param character: dictionary of representing the character and their attributes with
                    keys X-Coordinate, Y-Coordinate, Current HP, Current XP, &  Knowledge
    :precondition board: must be a dictionary with a tuple of integers representing coordinates as keys
    :precondition board: values must be strings
    :precondition character: must be dictionary of representing the character and their attributes with string
            keys: X-Coordinate, Y-Coordinate, Current HP, Current XP, &  Knowledge
    :precondition character: all dictionary values must be integers except for the one associated with "Knowledge"
                    which must be a string either "Novice", "Bookworm" or "Master Custodian"
    :precondition character: must be not none type
    :postcondition: obtains player's current location to acquire room's description from board and prints it
    :raise: KeyError if the character is missing a required attribute

    >>> board_one = {(0, 0): "Potato", (0,1): "Pie", (1, 0): "Cheese", (1,1): "Burger"}
    >>> character_one = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
    >>> describe_current_location(board_one, character_one)
    Burger
    >>> board_one = {(0, 0): "Potato", (0,1): "Pie"}
    >>> character_one = {"X-coordinate": 0 , "Y-coordinate": 0, "Current HP": 5}
    >>> describe_current_location(board_one, character_one)
    Potato
    >>> board_one = {(0, 0): "Lexus LFA"}
    >>> character_one = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
    >>> describe_current_location(board_one, character_one)
    Lexus LFA
    """
    stat_list = ['X-coordinate', 'Y-coordinate']
    for attribute in stat_list:
        if attribute not in list(character.keys()):
            raise KeyError("Character Attribute not found")

    try:
        description = board[(character["X-coordinate"], character["Y-coordinate"])]
    except KeyError as e:
        print(e)
    else:
        print(description)


def move_character(character: dict, direction: str):
    """
    Update character's location.

    This function updates the characters position on the board based on the direction chosen.

    :param character: dictionary of representing the character and their attributes including X-Coordinate, Y-Coordinate
                        Current HP, Current XP, &  Knowledge
    :param direction: a string for the direction to move the player towards
    :precondition character: must be dictionary of representing the character and their attributes with string
                            keys: X-Coordinate, Y-Coordinate, Current HP, Current XP, &  Knowledge
    :precondition character: all dictionary values must be integers except for the one associated with "Knowledge"
                            which must be a string either "Novice", "Bookworm" or "Master Custodian"
    :precondition direction: must be a string of 'N','E','S', or 'W'
    :postcondition: updates character's coordinates correctly according to direction the player moves in
    :raise: KeyError if the character is missing a required attribute

     >>> character_one = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
     >>> direction_one = "S"
     >>> move_character(character_one, direction_one)
     >>> print(character_one["Y-coordinate"])
     1
     >>> character_two = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 50, "Current XP": 50, "Knowledge": "bob"}
     >>> direction_two ="W"
     >>> move_character(character_two, direction_two)
     >>> print(character_two["X-coordinate"])
     1
    """
    stat_list = ['X-coordinate', 'Y-coordinate']
    for attribute in stat_list:
        if attribute not in list(character.keys()):
            raise KeyError("Character Attribute not found")

    # No need to raise errors for direction, because validate_move() does so
    if direction == "N":
        character["Y-coordinate"] -= 1
    elif direction == "S":
        character["Y-coordinate"] += 1
    elif direction == "E":
        character["X-coordinate"] += 1
    elif direction == "W":
        character["X-coordinate"] -= 1


def main():
    """
    Drive the program.
    """
    pass


if __name__ == "__main__":
    main()
