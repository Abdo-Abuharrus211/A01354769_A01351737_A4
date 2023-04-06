"""
 This module checks if the player wants to load a save file or start a new game
"""
from Progression_and_Save_files.reload_character import revive_character
from assets import make_character


def load_char_or_new():
    """
    Check if player wants to start new game or load save file and spawn character accordingly
    :precondition: user will only enter '1' or '2'
    :postcondition: Determine how the player would like to start the game based on their input
    :return: a dictionary to spawn the character from a JSON save file or by creating a new one
    """
    user_choice = int(input("Welcome to Cata! Let's begin, choose '1' or '2':\n1 - New Game.\n2 - Load Game."))
    # TODO: should we add a 'q' option here too???
    if user_choice == 1:
        character = make_character()
    elif user_choice == 2:
        character = revive_character()
    else:
        raise ValueError("Option not available. Please select 1 or 2")

    return character


def main():
    """
    Drive the program
    """


if __name__ == "__main__":
    main()
