# "QUIT to end the game"
from assets import make_character
import json


def store_character(character):
    """
    Stores the character if selected.

    This function stores the character stats when the user quits the game, if they choose to

    :param character:
    :return:
    """
    selection = input("You chose to quit the game, are you sure? Please type Y if you really want to "
                      "quit (or any other key to not)").upper()
    if selection == "Y":
        save_selection = input("Would you like to save your character? PLease type Y or N").upper()
        if save_selection == "N":
            character["Current HP"] = 0
        elif selection == "Y":
            filename = 'current_character.json'
            with open(filename, 'w') as file_object:
                json.dump(character, file_object)
            print("your game was saved")
            character["Current HP"] = 0
        else:
            print("Please select Y or N")
    else:
        return


def revive_character():
    """

    :return:
    """
    selection = input("Do you want to reload your previous character? Select Y or N ").upper()
    if selection == "N":
        make_character()
    elif selection == "Y":
        filename = 'current_character.json'
        with open(filename) as file_object:
            character = json.load(file_object)
            return character


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()
