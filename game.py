"""
Abdo & Kate make a game for A4
"""
from Kate_code import guessing_game, check_for_final_boss, final_boss
from assets import make_board, make_character

import assets
import game_mechanics
import game_state_control
import dialog
from user_io import get_user_choice


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
            game_mechanics.move_character(character, direction)
            game_mechanics.describe_current_location(board, character)
            # TODO I'm thinking of checking current HP in the boss version of check_for_foes and running from here?
            # TODO function is in Kate-Code
            there_is_a_challenger = game_state_control.check_for_foes()
            print()
            if there_is_a_challenger:
                guessing_game(character)
            game_state_control.level_up(character)
            # TODO: Where to add final boss call
            # achieved_goal = check_victory(board, character) # No need to check for achieved goal cuz only win boss
        if not game_state_control.dead_yet(character) and achieved_goal:
            # Print something to user here upon game completion here...
            break
        # check if alive and not ready for boss.
        elif not game_state_control.dead_yet(character) and not check_for_final_boss(character):
            print("Our trek continues little one.")

        # check if alive and not ready for boss.
        elif not game_state_control.dead_yet(character) and check_for_final_boss(character):
            print("It's Caraxes the Python of the Courtyard!!!!")  # TODO: add drama here...
            final_boss(character)
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
