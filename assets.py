"""
Asset creation module
"""

import random


def make_board(rows: int, columns: int) -> dict:
    """
    Create the game space.

    :param rows: integer greater than 2
    :param columns: integer greater than 2
    :precondition rows: must be an integer greater than 2
    :precondition columns: must be an integer greater than 2
    :postcondition: creates a dictionary that defines the map of the gam
    :raise ValueError: raises ValueError if either row or column input is not an integer greater than 2
    :return: dictionary of the map for the game

    """

    if rows != 10 or columns != 10:
        raise ValueError("Rows and columns must both be 10")

    else:
        list_rows = list(range(0, rows))
        list_columns = list(range(0, columns))
        board = {}
        for row_item in list_rows:
            for column_item in list_columns:
                board[row_item, column_item] = random.randint(1, 9)
        return board


def make_character() -> dict:
    """
    Create character attributes.

    :precondition: values for X-coordinate, Y-coordinate and Current HP must be integers
    :postcondition: creates dictionary with character attributes
    :return: dictionary with character attributes

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """

    player = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 0, "Knowledge": 1}
    return player


def main():
    """
    Drives the program
    """

    game()


if __name__ == "__main__":
    main()
