"""
Abdo & Kate make a game for A4
"""
import playsound as playsound

from Progression_and_Save_files.load_or_new_game import load_char_or_new
from Progression_and_Save_files.reload_character import save_character
from guessing_game import guessing_game
from game_user_io import get_user_choice, final_boss
from game_state_control import check_for_final_boss
from assets import make_board
from dialog import SPACER, ASCENSION_TIME, END

import game_mechanics
import game_state_control
import dialog

import time


def game():
    """
    Initiate the game loop and don't end it until player Wins or Game Over.
    """
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    # Here we call on the load/new function
    character = load_char_or_new()
    # character = make_character()
    direction = ""
    achieved_goal = False
    quit_game = False
    for _ in range(3):
        # print('Compiling Encyclopedias and Compendiums.')
        print('Tick')
        time.sleep(1)
        print('Tock')
        time.sleep(1)
    playsound.playsound("Audio/bgmusic.mp3", block=False)
    print(dialog.WELCOME_MESSAGE)
    while not achieved_goal:
        print(SPACER)
        print(f"\nWe're currently at({character['X-coordinate']},{character['Y-coordinate']})")
        try:
            direction = get_user_choice()
        except ValueError or KeyError as e:
            print(e)
        valid_move = False

        if direction == "Q":
            quit_game = save_character(character)
        if quit_game:
            break
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
        if character["Knowledge"] == "Master Custodian":
            print(SPACER)
            print(ASCENSION_TIME)
            print(SPACER)
        if not game_state_control.dead_yet(character) and check_for_final_boss(character):
            print("It's Caraxes the Python of the Courtyard!!!!")  # TODO: add drama here...
            final_boss(character)
            achieved_goal = True
            print(END)
        elif not game_state_control.dead_yet(character) and not check_for_final_boss(character):
            print("Our trek continues little one.")
        else:
            print("GAME OVER! You Perished...")
            break

    print("Thanks for playing")


def main():
    """
    Start the game
    """
    game()


if __name__ == "__main__":
    main()
