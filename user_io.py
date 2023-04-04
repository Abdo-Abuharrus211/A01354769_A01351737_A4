"""
    For functions that interact with the player.
"""
import random
from assets import make_enemy
from game_state_control import damage_received
# from questions_dictionary import questions_level_1, questions_level_2, questions_level_3


def get_user_choice() -> str:
    """
    Asks the player which direction they want to move towards.

    :precondition: player must only enter 'N','E','S', or 'W' directions when prompted
    :postcondition: receives player's input and assigns it to a variable, and raises error if player misbehaves
    :return: a string for the direction the player wishes to move towards
    :raises ValueError: if player enters anything besides 'N','E','S', or 'W""
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
                raise ValueError("\nWe mustn't wander astray!\nWe need to head in a direction that's on our path.")
    return player_movement


def final_boss(character: dict):
    """
    Play quiz with final boss

    This function plays a game where the user must select the correct answer.

    :param character: dictionary of character attributes containing string keys X-coordinate, Y-coordinate and
                    current HP with integer values
    :precondition character: must be a dictionary of character attributes
                             containing string keys X-coordinate, Y-coordinate and current HP
    :precondition character: all dictionary values must be integers
    :postcondition: prints appropriate message
    :postcondition: character HP goes to 0
    """
    #
    # print("Which of the following, In infinite Jest, is not something you would learn from spending time "
    #       "in a halfway house?\n"
    #       "1: That, perversely, it is often more fun to want something than to have it\n"
    #       "2: That you cannot win all of the time \n"
    #       "3: That everybody is identical in their secret, unspoken belief that way deep down, they are \n"
    #       "different from everyone else\n"
    #       "4: That certain persons simply will not like you, no matter what you do\n"
    #       "That there is such a thing as raw, unalloyed, agendaless kindness")

    try:
        answer = int(input("Which of the following, In infinite Jest, is not something you would learn from "
                           "spending time in a halfway house?\n "
                           "1: That, perversely, it is often more fun to want something than to have it\n"
                           "2: That you cannot win all of the time \n"
                           "3: That everybody is identical in their secret, unspoken belief that way"
                           "deep down, they are \n"
                           "different from everyone else\n"
                           "4: That certain persons simply will not like you, no matter what you do\n"
                           "That there is such a thing as raw, unalloyed, agendaless kindness \n"
                           "Choose your answer little one"))
    except ValueError:
        print("You did not chose an answer in range, game over")
        character["Current HP"] = 0
    else:
        if answer < 1 or answer > 5:
            print("You did not chose an answer in range, game over")
            character["Current HP"] = 0
        elif answer == 2:
            print("Congratulations, you won!")
        elif answer != 2:
            print("Incorrect, Caraxes has constricted the light out of you...I'm sorry little one")
            character["Current HP"] = 0


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
