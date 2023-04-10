"""
    For functions that interact with the player.
"""
import random

from Progression_and_Save_files.reload_character import save_character
from assets import make_enemy
from game_state_control import damage_received


# from questions_dictionary import questions_level_1, questions_level_2, questions_level_3


def get_user_choice() -> str:
    """
    Gets user direction choice.

    This function asks the player which direction they want to move towards.

    :precondition: player must only enter 'N','E','S', or 'W' directions when prompted or 'Q' to quit game
    :postcondition: receives player's input and assigns it to a variable
    :return: a string for the direction the player wishes to move towards
    :raises ValueError: if player enters anything besides 'N','E','S', 'W'  or 'Q'
    """
    accepted_directions = ("N", "E", "S", "W")
    directions_dict = {"N": "North", "E": "East", "S": "South", "W": "West", "Q": "Quit"}
    player_choice = ""
    need_direction = True
    while need_direction:
        if player_choice == "" or player_choice not in accepted_directions:
            player_choice = input(
                "Which way would you like to go?\nRemember, your map scroll only accepts:\n"
                " 'N' for North\n 'E' for East\n 'S' for South\n 'W' for West\n\n 'Q' for Quit game\n").upper()
            if player_choice in accepted_directions and player_choice != "Q":
                need_direction = False
                print(f"Heading {directions_dict[player_choice]}, off we go!")
            elif player_choice == "Q":
                return player_choice
            else:
                raise ValueError("\nWe mustn't wander astray!\nWe need to head in a direction that's on our path.")
    return player_choice


def final_boss(character: dict):
    """
    Play quiz with final boss

    This function plays a game where the user must select the correct answer.

    :param character: dictionary of representing the character and their attributes including X-Coordinate, Y-Coordinate
                        Current HP, Current XP, &  Knowledge
    :precondition character: dictionary of representing the character and their attributes including X-Coordinate,
                            Y-Coordinate Current HP, Current XP, &  Knowledge
    :precondition character: all dictionary values must be integers except for Knowledge values must be a String
    :postcondition: prints appropriate message
    :postcondition: set character HP to 0
    :raises ValueError: if the player does not choose an input of the given options
    """
    try:
        answer = int(input("According to David Foster Wallace, in Infinite Jest, if, "
                           "by the virtue of charity or the circumstances of desperation, you ever chance to spend \n"
                           "a little time around a Substance-recovery halfway facility, what is an exotic new "
                           "fact you may NOT aquire? \n "
                           "1: That, perversely, it is often more fun to want something than to have it\n"
                           "2: That you cannot win all of the time \n"
                           "3: That everybody is identical in their secret, unspoken belief that way"
                           "deep down, they are \n"
                           "different from everyone else\n"
                           "4: That certain persons simply will not like you, no matter what you do\n"
                           "5: That there is such a thing as raw, unalloyed, agendaless kindness \n"
                           "Choose your answer little one"))
    except ValueError:
        print(f"You did not chose an answer in range, game over")
        character["Current HP"] = 0
    else:
        if answer < 1 or answer > 5:
            print(f"You did not chose an answer in range, game over")
            character["Current HP"] = 0
        elif answer == 2:
            print(f"Congratulations, you won!")
        elif answer != 2:
            print(f"Incorrect, Caraxes has constricted the light out of you...I'm sorry little one")
            character["Current HP"] = 0


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
