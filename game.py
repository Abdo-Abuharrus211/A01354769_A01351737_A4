"""
Abdo & Kate make a game for A4
"""


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

    print("---------------------------------------------------------------------------------\n"
          "Brave One, did you hear? The White Wolf himself sent for our aid.\n"
          "We must set out at once, Master Geralt needs us!\n")
    while not achieved_goal:
        describe_current_location(board, character)
        print(f"\nWe're currently at({character['X-coordinate']},{character['Y-coordinate']})")

        try:
            direction = get_user_choice()
        except ValueError or KeyError as e:
            print(e)
        valid_move = False

        try:
            valid_move = validate_move(board, character, direction)
        except KeyError as e:
            print(e)

        if valid_move:
            move_character(character, direction)
            describe_current_location(board, character)
            there_is_a_challenger = check_for_foes()
            if there_is_a_challenger:
                duelling_game(character)
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
    Start game
    """


if __name__ == "__main__":
    main()
