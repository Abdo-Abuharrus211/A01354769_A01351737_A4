"""
    For functions that interact with the player.
"""
import random


def get_user_choice() -> str:
    """
    Asks the player which direction they want to move towards.

    :precondition: player must only enter 'N','E','S', or 'W' directions when prompted
    :postcondition: receives player's input and assigns it to a variable, and raises error if player misbehaves
    :return: a string for the direction the player wishes to move towards
    :raises ValueError: if player enters anything besides 'N','E','S', or 'W'
    """
    accepted_directions = ("N", "E", "S", "W")
    directions_dict = {"N": "North", "E": "East", "S": "South", "W": "West"}
    player_movement = ""
    need_direction = True

    while need_direction:

        if player_movement == "" or player_movement not in accepted_directions:
            player_movement = input(
                "Which way would you like to go?\nRemember, your map scroll only accepts:\n"
                " 'N' for North\n 'E' for East\n 'S' for South\n 'W' for West\n ").upper()
            if player_movement in accepted_directions:
                need_direction = False
                print(f"Heading {directions_dict[player_movement]}, off we go!")
            else:
                raise ValueError("\nWe mustn't wander astray!\nWe need to head on a direction that's on our path.")
    return player_movement


def main():
    """
    Drive the program.
    """
    pass


if __name__ == "__main__":
    main()
