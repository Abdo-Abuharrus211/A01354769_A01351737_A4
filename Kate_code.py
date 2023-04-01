import random

from assets import make_enemy
from questions_dictionary import questions_level_1, questions_level_2, questions_level_3


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

    # TODO: Kate's question guessing game, troubleshoot and fix together consulting Chris
    # Once matter is resolved, then can work together on this. Refer to the flowchart and game diagram

    player_level = character["Knowledge"]
    if player_level == 1:
        current_dictionary = questions_level_1
        pass
    elif player_level == 2:
        current_dictionary = questions_level_2
        pass
    else:
        current_dictionary = questions_level_3

    # current_dictionary = (f"questions_level_{player_level:.0f}").format(player_level)  # What's this doing?
    question = random.choice(list(current_dictionary))
    print(make_enemy())
    # print("You have met an enemy who wants to ask you a question!\n", question)
    print("You must answer the question to persevere! \n", question)
    try:
        answer = int(input("Choose your answer little one: "))
    except ValueError:
        print("'Please pick a number between 1 and 5 inclusive, you lost 1 HP'")
        character["Current HP"] -= 1
    else:
        if answer < 1 or answer > 5:
            print("'Please pick a number between 1 and 5 inclusive, you lost 1 HP'")
            character["Current HP"] -= 1
        elif answer == current_dictionary[question]:
            character["Current XP"] += 20
            print("You may pass unharmed")
        elif answer != current_dictionary[question]:
            print("'Incorrect, 1 hit taken'")
            character["Current HP"] -= 1


def check_for_final_boss(character: dict) -> bool:
    """
    Determine if there's a 20% chance to face and fight a foe to fight by generating a random integer.

    :postcondition: generates random integer in a specific range then check if it's equal or greater than 25%
    :return: True if there's a 20% or more chance of facing a foe, return False otherwise
    """
    if character["Current XP"] >= 400:
        return True
        # return random.randint(1, 10) <= 2
    else:
        return False


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

    print("Which of the following, In infinite Jest, is not something you would learn from spending time "
          "in a halfway house?\n"
          "1: That, perversely, it is often more fun to want something than to have it\n"
          "2: That you cannot win all of the time \n"
          "3: That everybody is identical in their secret, unspoken belief that way deep down, they are \n"
          "different from everyone else\n"
          "4: That certain persons simply will not like you, no matter what you do\n"
          "That there is such a thing as raw, unalloyed, agendaless kindness")

    try:
        answer = int(input("Choose your answer little one"))
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
    guessing_game({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 7, "Current XP": 400, "Knowledge": 2})


if __name__ == "__main__":
    main()
