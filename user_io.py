"""
    For functions that interact with the player.
"""


def get_user_choice() -> str:
    """
    Asks the player which direction they want to move towards.

    :precondition: player must only enter 'N','E','S', or 'W' directions when prompted
    :postcondition: receives player's input and assigns it to a variable, and raises error if player misbehaves
    :return: a string for the direction the player wishes to move towards
    :raises ValueError: if player enters anything besides 'N','E','S', or 'W'
    """
    accepted_directions = ("N", "E", "S", "W")
    directions_dict = {"N": "North", "E": "East", "S": "South", "W": "West"}
    player_movement = ""
    need_direction = True

    while need_direction:

        if player_movement == "" or player_movement not in accepted_directions:
            player_movement = input(
                "Which way would you like to go?\nRemember, the enchanted Koviri compass only accepts:\n"
                " 'N' for North\n 'E' for East\n 'S' for South\n 'W' for West\n ").upper()
            if player_movement in accepted_directions:
                need_direction = False
                print(f"Heading {directions_dict[player_movement]}, off we go!")
            else:
                raise ValueError("\nThat's not a compass bearing you dimwit!\nWe need a direction.")
    return player_movement


def duelling_game(character: dict):
    """
    Prompt player to guess the correct number within a specified range to defeat the foe.

    :param character: dictionary representing player's character stats, current location and HP
    :precondition: character is valid dictionary containing character's stats and not None type
    :postcondition: starts a single round of a guessing game, player must guess for a random integer in a range,
    and check if player's guess is correct or not, deducts 1 point from HP if they guess wrong
    """
    print("A foe is here! You must use the Staff of Shaerrawedd's Tears of to guess the number and trick them.")
    lower = 1
    upper = 5
    possibilities = [1, 2, 3, 4, 5]
    secret_number = str(random.randint(lower, upper))
    guess = input(f"Enter a number between {lower} and {upper} inclusive: ")
    # guess = int(user_input)

    if guess.isdigit() and int(guess) in possibilities:
        if guess == secret_number:
            print("Hurray! You've beat the troll at his own game!")
        elif guess < secret_number:
            print(f"Too low, the number was {secret_number}, shield yourself!\n")
            character["Current HP"] -= 1
        elif guess > secret_number:
            print(f"Too high, the number was {secret_number}, shield yourself!\n")
            character["Current HP"] -= 1
    else:
        print("That wasn't a number you dolt! Now we must fight the troll.\n")
        character["Current HP"] -= 1
