# "QUIT to end the game"
from assets import make_character
import json


def save_character(character: dict):
    """
    Save the current character if selected.

    This function stores the character stats and progression when the user quits the game, if they choose to

    :param character: dictionary of representing the character and their attributes including X-Coordinate, Y-Coordinate
            Current HP, Current XP, &  Knowledge
    :precondition: character must be a dictionary of representing the character and their attributes including
                    X-Coordinate, Y-Coordinate Current HP, Current XP, &  Knowledge
    :return: True if game is quit (saved or not), False otherwise
    """
    # TODO: I think this does too much, quitting and saving and printing. it should save only I think
    selection = input("You chose to quit the game, are you sure? Please type Y if you really want to "
                      "quit (or any other key to not)").upper()
    if selection == "Y":
        save_selection = input("Would you like to save your character? PLease type Y or N").upper()
        if save_selection == "N":
            return True
        elif selection == "Y":
            filename = 'Progression_and_Save_files/saved_character.json'
            with open(filename, 'w') as file_object:
                json.dump(character, file_object)
            print("your game was saved")
            return True
        else:
            print("Please select Y or N")
    else:
        return False


def load_character():
    """
    Load previously saved character from JSON file.

    :precondition: save file must exist
    :postcondition: loads character dictionary from the JSON save file
    :return: loaded character dictionary
    """
    selection = input("Do you want to reload your previous character? Select Y or N ").upper()
    if selection == "N":
        make_character()
    elif selection == "Y":
        filename = 'Progression_and_Save_files/saved_character.json'
        with open(filename) as file_object:
            character = json.load(file_object)
            return character


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
