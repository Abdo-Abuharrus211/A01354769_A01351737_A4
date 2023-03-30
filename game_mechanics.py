"""
    This module is for functions that comprise the game's core elements and mechanics.
"""


def describe_current_location(board: dict, character: dict):
    """
    Describe the room the player is currently in.

    :param board: dictionary representing the game board's rooms, with (x,y) coordinates as keys and string values.
    :param character: dictionary representing player's character stats, current location and HP
    :precondition: board and character are dictionaries and not None types
    :postcondition: obtains player's current location to acquire room's description from board and prints it
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
    try:
        description = board[(character["X-coordinate"], character["Y-coordinate"])]
    except KeyError as e:
        print(e)
    else:
        print(description)


def move_character(character: dict, direction: str):
    """
    Update character's current location on the board.

    :param character: dictionary representing player's character stats, current location and HP
    :param direction: a string for the direction to move the player towards
    :precondition: character is valid dictionary with character stats, and direction is a string of 'N','E','S', or 'W'
    :postcondition: updates character's coordinates correctly according to direction the player moves in
     >>> character_one = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
     >>> direction_one = "S"
     >>> move_character(character_one, direction_one)
     >>> print(character_one["Y-coordinate"])
     1
    """
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
