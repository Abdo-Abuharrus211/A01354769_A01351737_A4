"""
Abdo & Kate make a game for A4
"""
from user_io import get_user_choice, guessing_game, final_boss
from game_state_control import check_for_final_boss
from assets import make_board, make_character
from dialog import SPACER

import game_mechanics
import game_state_control
import dialog


def game():
    """
    Initiate the game loop and don't end it until player Wins or Game Over.
    """
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character()
    direction = ""
    achieved_goal = False
    print(dialog.WELCOME_MESSAGE)
    while not achieved_goal:
        print(SPACER)
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
            game_mechanics.move_character(character, direction)
            game_mechanics.describe_current_location(board, character)

            there_is_a_challenger = game_state_control.check_for_foes()
            if there_is_a_challenger:
                guessing_game(character)
            game_state_control.level_up(character)

        if not game_state_control.dead_yet(character) and check_for_final_boss(character):
            print("It's Caraxes the Python of the Courtyard!!!!")  # TODO: add drama here...
            final_boss(character)
            achieved_goal = True
        elif not game_state_control.dead_yet(character) and not check_for_final_boss(character):
            print("Our trek continues little one.")
        else:
            print("YOU DIED")
            break
    print("\nThanks for playing.")


def main():
    """
    Start the game
    """
    game()


if __name__ == "__main__":
    main()
