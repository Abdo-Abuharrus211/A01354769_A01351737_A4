"""
Asset creation module
"""

import random


def make_description() -> str:
    """
    Generate random description from a list of descriptions.

    :postcondition: generate random integer to index through a list and obtain a room description
    :return: a random string from the collection of strings
    """
    # TODO: Add more room descriptions ~ 40-50
    room_descriptions = ("The dusty scrolls of the stacks howled with an eerie silence",
                         "It seems a family of jumping spiders are practicing parkour")
    return room_descriptions[random.randint(0, len(room_descriptions) - 1)]


def make_enemy() -> str:
    """
    Generate random description for enemies.

    :postcondition: generate random integer to index through a list and obtain an enemy description
    :return: a random string from the collection of strings
    """
    # TODO: Add more enemy descriptions ~ 20
    enemy_descriptions = ("Look out, it's a warrior ant with ill intentions!",
                          "The Snail of Orwell demands a duel!")
    return enemy_descriptions[random.randint(0, len(enemy_descriptions) - 1)]


def make_board(rows: int, columns: int) -> dict:
    """
    Create the game space.

    :param rows: integer greater than 2
    :param columns: integer greater than 2
    :precondition rows: must be an integer greater than 2
    :precondition columns: must be an integer greater than 2
    :postcondition: creates a dictionary that defines the map of the game
    :raise ValueError: raises ValueError if either row or column input is not an integer greater than 2
    :return: dictionary of the map for the game
    """
    if rows != 10 or columns != 10:
        raise ValueError("Rows and columns must both be 10")

    else:
        game_board = {(row, column): make_description() for row in range(rows) for column in range(columns)}
        return game_board


def make_character() -> dict:
    """
    Create character attributes.

    :precondition: values for X-coordinate, Y-coordinate and Current HP must be integers
    :postcondition: creates dictionary with character attributes
    :return: dictionary with character attributes

    >>> make_character()
    {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 0, "Knowledge": 1}
    """
    player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 0, "Knowledge": " "}
    return player


def main():
    """
    Drive the program
    """


if __name__ == "__main__":
    main()
