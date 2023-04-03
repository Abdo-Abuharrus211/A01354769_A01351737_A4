"""
    For functions that interact with the player.
"""
import random
from assets import make_enemy
from questions_dictionary import questions_level_1, questions_level_2, questions_level_3


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


def get_question(character: dict):
    """
    Get the question and answer for enemy quiz

    This function will get a random question and correct answer from the appropriate dictionary based on character Level
    :param character:
    :precondition:
    :return: the answer of the question
    """
    player_level = character["Knowledge"]
    if player_level == "Novice":
        current_dictionary = questions_level_1
    elif player_level == "Bookworm":
        current_dictionary = questions_level_2
    else:
        current_dictionary = questions_level_3
    question = random.choice(list(current_dictionary))
    real_answer = current_dictionary[question]
    print(make_enemy(), "You must answer the question to persevere! \n", question)
    return real_answer


def guessing_game(character: dict):
    """
    Play a guessing game

    This function plays a guessing game where the player has to guess a randomly selected number between 1 and 5.

    :param character: dictionary of character attributes containing string keys X-coordinate, Y-coordinate and
                    current HP with integer values
    :precondition character: must be a dictionary of character attributes
                             containing string keys X-coordinate, Y-coordinate and current HP
    :precondition character: all dictionary values must be integers
    :postcondition: update to character dictionary if appropriate
    """
    real_answer = get_question(character)
    try:
        answer = int(input("Choose your answer little one: "))
    except ValueError:
        print("'Please pick a number between 1 and 5 inclusive, you lost 1 HP'")
        character["Current HP"] -= 1
    else:
        if answer < 1 or answer > 5:
            print("'Please pick a number between 1 and 5 inclusive, you lost 1 HP'")
            character["Current HP"] -= 1
        elif answer == real_answer:
            character["Current XP"] += 20
            print("You may pass unharmed")
        elif answer != real_answer:
            print("'Incorrect, 1 hit taken'")
            character["Current HP"] -= 1


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
            print("Incorrect, game over")
            character["Current HP"] = 0


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
