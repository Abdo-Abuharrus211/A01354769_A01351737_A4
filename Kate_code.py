def describe_current_location(board: dict, character: dict, rows: int, columns: int) -> None:
    """
    Describes character location.

    This function describes the current location of the character on the board based on the dictionary.

    :param board: dictionary of the game space with coordinates as keys and integers as values
    :param character: dictionary of character attributes containing X-coordinate, Y-coordinate and current HP
    :param rows: integer greater than 2
    :param columns: integer greater than 2
    :precondition rows: must be integer greater than 2
    :precondition columns: must be integer greater than 2
    :precondition board: must b`e dictionary of the game space with coordinates as keys and integers as values
    :precondition character: must be a dictionary of character attributes
                    containing string keys X-coordinate, Y-coordinate and current HP
    :precondition character: all dictionary values must be integers
    :raise ValueError: raises ValueError if the player is not within the game space defined by board
    :postcondition: prints the appropriate location description based on character location

    >>> test_character = {"X-coordinate": 0, "Y-coordinate": 2, "Current HP": 5}
    >>> test_board = {(0, 0): 3, (0, 1): 7, (0, 2): 9, (1, 0): 6, (1, 1): 5, (1, 2): 9, (2, 0): 8, (2, 1): 4, (2, 2): 4}
    >>> (describe_current_location(test_board, test_character, 3, 3))
    Oh no it looks like it's going to rain!
    >>> test_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
    >>> test_board = {(0, 0): 3, (0, 1): 7, (0, 2): 9, (1, 0): 6, (1, 1): 5, (1, 2): 9, (2, 0): 8, (2, 1): 4, (2, 2): 4}
    >>> (describe_current_location(test_board, test_character, 3, 3))
    You have encountered some thick vines, good thing you brought a knife

    """
    if character["X-coordinate"] < 0 or character["X-coordinate"] >= columns:
        raise ValueError("The player is not within the board!")
    if character["Y-coordinate"] < 0 or character["Y-coordinate"] >= rows:
        raise ValueError("The player is not within the board!")

    description_rooms = {1: "There is a house up on the hill ahead",
                         2: "You are now in the jungle, watch our for tigers!",
                         3: "You are now at a fast flowing river, hope you can swim",
                         4: "You have arrived at a sunny rock, have a rest and recharge",
                         5: "You have encountered some thick vines, good thing you brought a knife",
                         6: "Oh that is a big hill, take your time to climb it",
                         7: "You are in an open field, watch out for snakes!",
                         8: "Night is beginning to fall, hope you find your way home soon",
                         9: "Oh no it looks like it's going to rain!"}

    current_location = board[character["X-coordinate"], character["Y-coordinate"]]
    print(description_rooms[current_location])


def get_user_choice():
    """
    Return user input

    :precondition: must input integer between 1 and 4 inclusive
    :postcondition: returns the direction chosen by player
    :return: chosen direction as a string

    """

    player_choice = (input("Choose a number for direction: \n 1: Up \n 2: Down \n 3: Left \n 4: Right: "))
    if player_choice == "1" or player_choice == "2" or player_choice == "3" or player_choice == "4":
        chosen_input = player_choice
        return chosen_input
    else:
        chosen_input = "You stay still. Please choose a number 1 to 4 to describe the direction you want to go"
        print("You stay still. Please choose a number 1 to 4 to describe the direction you want to go")
        return chosen_input


def validate_move(rows: int, columns: int, character: dict, direction: str) -> bool:
    """
    Checks user input is valid.

    :param rows: positive integer greater than 2
    :param columns: positive integer greater than 2
    :param character:dictionary of character attributes containing X-coordinate, Y-coordinate and current HP
    :param direction: string of either 1, 2, 4 or 4
    :precondition rows: must be a positivie integer greater than 2
    :precondition columns: must be a positivie integer greater than 2
    :precondition character: must be a dictionary of character attributes
                            containing string keys X-coordinate, Y-coordinate and current HP
    :precondition character: all dictionary values must be integers
    :precondition direction: must be a string of value either 1, 2, 3 or 4
    :return: True if user input is valid, False otherwise

    >>> validate_move(3, 3, {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}, "3")
    False
    >>> validate_move(3, 3, {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}, "2")
    True
    """

    if character["X-coordinate"] == 0 and direction == "3":
        return False
    elif character["X-coordinate"] == (rows - 1) and direction == "4":
        return False
    elif character["Y-coordinate"] == (columns - 1) and direction == "2":
        return False
    elif character["Y-coordinate"] == 0 and direction == "1":
        return False
    else:
        return True


def move_character(character: dict, direction: str) -> None:
    """
    Update character's location.

    This function updates the character's location on the board.

    :param character: dictionary of character attributes containing string keys X-coordinate, Y-coordinate and
    current HP with integer values
    :param character: dictionary of chara
    :param direction: string of either 1 , 2 , 3 or 4
    :precondition character: must be a dictionary of character attributes
                             containing string keys X-coordinate, Y-coordinate and current HP
    :precondition character: all dictionary values must be integers
    :precondition direction: must be string of either 1 , 2 , 3 or 4
    :postcondition: update the appropriate coordinate in character dictionary

    >>> test_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> move_character(test_character, "2")
    >>> print(test_character)
    {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}

    >>> test_character = {'X-coordinate': 2, 'Y-coordinate': 0, 'Current HP': 5}
    >>> move_character(test_character, "3")
    >>> print(test_character)
    {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}

    """

    if direction == "1":
        character["Y-coordinate"] -= 1
    elif direction == "2":
        character["Y-coordinate"] += 1
    elif direction == "3":
        character["X-coordinate"] -= 1
    elif direction == "4":
        character["X-coordinate"] += 1


def check_if_goal_attained(rows: int, columns: int, character: dict) -> bool:
    """
    Check if the game will end.

    This function checks if the user has reached the goal destination or not.

    :param rows: integer greater than 2
    :param columns: integer greater than 2
    :param character: dictionary of character attributes containing string keys X-coordinate, Y-coordinate and
                    current HP with integer values
    :precondition rows: must be integer greater than 2
    :precondition columns: must be integer greater than 2
    :precondition character: must be a dictionary of character attributes
                    containing string keys X-coordinate, Y-coordinate and current HP
    :precondition character: all dictionary values must be integers
    :postcondition: returns true or false as appropriate for character location
    :return: either True or False

    >>> check_if_goal_attained(3, 3, {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5})
    False
    >>> check_if_goal_attained(3, 3, {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 4})
    True
    """
    if character["X-coordinate"] == (rows - 1) and character["Y-coordinate"] == (columns - 1):
        return True
    else:
        return False


def check_for_foes() -> bool:
    """
    Determine if the player encounters a foe

    :postcondition:  returns True 25% of the time, False otherwise
    :return: True if foe is encountered, else False
    """
    is_there_foe = random.randint(1, 4)
    if is_there_foe == 1:
        return True
    else:
        return False


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

    player_level = character["Level"]
    if player_level == 1:
        question = random.choice(list(questions_level_1.items()))
    if player_level == 2:
        question = random.choice(list(questions_level_2.items()))
    if player_level == 3:
        question = random.choice(list(questions_level_3.items()))

    try:
        answer = int(input(" You met an enemy who wants to play a game! Enter a number between 1 and 5 inclusive:"))
    except ValueError:
        print("Please pick a number between 1 and 5 inclusive, you lost 1 HP")
        character["Current HP"] -= 1
    else:
        if answer ==
            print("Please pick a number between 1 and 5 inclusive, you lost 1 HP")
            character["Current HP"] -= 1
        elif guess == secret_number:
            print("You may pass unharmed")
        elif guess != secret_number:
            print("Incorrect, 1 hit taken")
            character["Current HP"] -= 1


def is_alive(character: dict) -> bool:
    """
    Determine if character is "alive"

    Determines if the character is alive by checking if the HP points are > 0

    :param character: dictionary of character attributes containing string keys X-coordinate, Y-coordinate and
                    current HP with integer values
    :precondition character: must be a dictionary of character attributes
                    containing string keys X-coordinate, Y-coordinate and current HP
    :precondition character: all dictionary values must be integers
    :postcondition: return appropraite boolean value
    :return: True if character is dead, False otherwise

    >>> is_alive({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 4})
    True
    >>> is_alive({"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 0})
    False

    """

    if character["Current HP"] != 0:
        return True
    else:
        return False
