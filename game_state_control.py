def check_for_foes() -> bool:
    """
    Determine if there's a 25% chance to face and fight a foe to fight by generating a random integer.

    :postcondition: generates random integer in a specific range then check if it's equal or greater than 25%
    :return: True if there's a 25% or more chance of facing a foe, return False otherwise
    """
    return random.randint(1, 20) >= 5


def dead_yet(character):
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


def check_victory(board, character):
    """
    Determine if the player is victorious and has reached the end point (bottom right corner) alive

    :param board: dictionary representing the game board's rooms, with (x,y) coordinates as keys and string values.
    :param character: dictionary representing player's character stats, current location and HP
    :precondition: board is valid dictionray containing board's specifications and character is valid dictionary
                    containing character's stats
    :postcondition: accurately determines if player is at the end point's coordinates
    :return: True if the player completes the game, return False otherwise
    >>> board_one = {(0, 0): "Potato", (0,1): "Pie", (1, 0): "Cheese", (1,1): "Burger"}
     >>> character_one = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
     >>> check_victory(board_one, character_one)
     False
     >>> board_one = {(0, 0): "Potato", (0,1): "Pie", (1, 0): "Cheese", (1,1): "Burger"}
     >>> character_one = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 2}
     >>> check_victory(board_one, character_one)
     False
     >>> board_one = {(0, 0): "Potato", (0,1): "Pie", (1, 0): "Cheese", (1,1): "Burger"}
     >>> character_one = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 0}
     >>> check_victory(board_one, character_one)
     True
     """
    if character["X-coordinate"] == max(board)[0] and character["Y-coordinate"] == max(board)[1]:
        return True
    else:
        return False
