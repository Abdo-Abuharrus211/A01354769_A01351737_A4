# "QUIT to end the game"
character = {"sfg": 0, "fsi3": 4}
# This code is for after quit has been inputted:
import json
def store_character(character):
    """

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
    else: return


def main():
    """
    Drive the program.
    """
    store_character(character)

if __name__ == "__main__":
    main()









