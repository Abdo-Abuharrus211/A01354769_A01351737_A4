"""
Abdo & Kate make a game for A4
"""
from assets import make_board, make_character


import assets
import game_mechanics
import game_state_control
import questions_dictionary
import dialog
from user_io import get_user_choice


def game():
    """
    Initiate the game loop and don't end it until Victory or Game Over.
    """
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character()
    direction = ""
    achieved_goal = False

    print(dialog.WELCOME_MESSAGE)
    while not achieved_goal:
        game_mechanics.describe_current_location(board, character)
        print(f"\nWe're currently at({character['X-coordinate']},{character['Y-coordinate']})")

        try:
            direction = get_user_choice()
        except ValueError or KeyError as e:
            print(e)
        valid_move = False

        try:
            valid_move = game_state_control.validate_move(board, character, direction)
        except KeyError as e:
            print(e)

        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                duelling_game(character)
            level_up(character)
            achieved_goal = check_victory(board, character)
        if not dead_yet(character) and achieved_goal:
            # Print something to user here upon game completion here...
            break
        elif not dead_yet(character) and not achieved_goal:
            print("Our quest lingers on...")
        else:
            print("YOU DIED")
            break
    print("\nThanks for playing.")


def main():
    """
    Start the game
    """


if __name__ == "__main__":
    main()
