# "QUIT to end the game"
#
# This code is for after quit has been inputted:
import json
def store_character(character):
    """

    :param character:
    :return:
    """
    selection = input("You chose to quit the game, are you sure? Please type Y or N to choose")
    if selection == "N":
        return
    elif selection == "Y":
        save_selection = input("Would you like to save your character? PLease type Y or N to choose")
        if save_selection == "N":
            character["Current HP"] = 0
        if selection == "Y":
            filename = 'current_character_.json'
            with open(filename, 'w') as file_object:
                json.dump(character, file_object)
            character["Current HP"] = 0








