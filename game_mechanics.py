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