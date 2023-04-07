import random

from assets import make_enemy
from game_state_control import damage_received


def guessing_game(character: dict):
    """
    Play a quiz game

    This function plays a quiz game where the player has to choose the correct answer.

    :param character: dictionary of representing the character and their attributes including X-Coordinate, Y-Coordinate
            Current HP, Current XP, &  Knowledge
    :precondition character: must be a dictionary of representing the character and their attributes including
                    X-Coordinate, Y-Coordinate Current HP, Current XP, &  Knowledge
    :precondition character: all dictionary values except for Knowledge must be integers
    :precondition: character Knowledge must either be 'Novice', 'Bookworm, or 'Master Custodian'
    :postcondition: update to character dictionary if appropriate
    :postcondition: prints the appropriate follow-up message to the player
    """

    def get_question(inner_character: dict):
        """
        Get the question and answer for enemy quiz

        This function will retrieve a random question and correct answer from the appropriate
         dictionary based on character Level
        :param inner_character: dictionary of representing the character and their attributes including X-Coordinate,
                                Y-Coordinate Current HP, Current XP, &  Knowledge
        :precondition: must be dictionary of representing the character and their attributes including X-Coordinate,
                        Y-Coordinate Current HP, Current XP, &  Knowledge
        :postcondition: prints the correct question to the player
        :return: the answer of the question
        """
        questions_level_1 = {"Shantaram (by Australian escaped criminal Gregory David Roberts)"
                             "is set in which country?\n 1: China\n 2: Indonesia\n 3: Japan \n 4: India \n 5: Nepal": 4,
                             "Alice Walker's famous book (also made into a movie): The Color ___ "
                             "\n 1: Red\n 2: Green\n 3: Yellow \n 4: Purple \n 5: Blue": 4,
                             "What is the answer to the meaning of life according to Hitchhikers Guide to the Galaxy? "
                             "\n 1: 100\n 2: 420\n 3: 42 \n 4: 1 \n 5: Infinity": 3,
                             "Which of the following is not a book by Malcolm Gladwell:"
                             "\n 1: Outwitting the Devil \n 2: The Tipping Point \n 3: Outliers \n 4: Talking to "
                             "Strangers \n 5:"
                             "Blink": 1,
                             "Which book is the shortest? "
                             "\n 1: Animal Farm \n 2: 1984\n 3: Lord of the Flies \n 4: Clockwork Orange \n 5: "
                             "Catch 22": 1,
                             "The TV show 'Big Brother' is based on the all-seeing entity from which book:"
                             "\n 1: To kill a Mockingbird \n 2: Da Vinci Code \n 3: Twenty "
                             "Thousand Legues Under the Sea \n 4: "
                             "After the Cure \n 5: 1984": 5,
                             "What is a supposedly fun thing that David Foster Wallace will never do again?"
                             "\n 1: Go on a cruise Ship \n 2: Oktoberfest in Germany \n 3: Run with the "
                             "bulls \n 4: Carnival "
                             "in Brazil "
                             "\n 5: New Years ball drop in New York ": 1,
                             }

        questions_level_2 = {"What are the main characters in Never Let Me Go? "
                             "\n 1: Clones\n 2: Humans\n 3: Robots \n 4: Faceless AI \n 5: Dream characters": 1,
                             "The Poisonwood Bible is predominantly set in what part of the world? "
                             "\n 1: Asia\n 2: Australia\n 3: South America \n 4: North America \n 5: Africa": 5,
                             "When the Body Says no (by Canadian doctor Gabor Mate) main message is: "
                             "\n 1: Always listen to your gut\n 2: If you don't rest you will get tired\n 3: "
                             "If you don't "
                             "look after your mental health, your physical health will suffer \n 4: Drugs are bad \n "
                             "5: Don't work out when you are tired": 2,
                             "Marching Powder is set in:"
                             "\n 1: Colombia \n 2: Bolivia\n 3: Mexico \n 4: Peru \n 5: Panama": 2,
                             "All the light we cannot see is set in:"
                             "\n 1: Space \n 2: WWI \n 3: The future \n 4: Ancient Greece \n 5: In dream": 2,
                             "Pain is inevitable, suffering is optional was made famous by:"
                             "\n 1: George Orwell \n 2: Haruki Murakami \n 3: Alice Walker \n 4: "
                             "Malcolm Gladwell \n 5: Dale"
                             " Carnegie": 2,
                             "'First, make the beast beautiful' is a book about:"
                             "\n 1: Beauty pageants \n 2: Anxiety  \n 3: Children \n 4: Overcoming loss"
                             " \n 5: High school": 2,
                             "What group of people are not researched / interviewed in Far from The Tree"
                             "\n 1: Criminals \n 2: Blind\n 3: Autistic \n 4: Genius \n 5: Little people": 2
                             }

        questions_level_3 = {"What is NOT presented as true in Breathe by James Nestor"
                             "\n 1: Mouth breathing is awful for you\n 2: Modern day diet negatively effects "
                             "our facial "
                             "structure\n "
                             "3: Having out-breath SHORTER than in-breath lowers anxiety \n 4: "
                             "Importance of breathe is highly "
                             "underrated"
                             "  \n 5: Most people are over-breathers (too fast and too shallow": 3,
                             "What movie / show actually complements the book really well "
                             "(subjective but also definitely a correct "
                             "answer :P) "
                             "\n 1: Cloud Atlas\n 2: Tomorrow When the War Began\n 3: The Hobbit \n 4: Hunger Games"
                             "Lord of the Rings \n 5: Rings of Power": 1,
                             "Which Haruki Murakmi novel has no fantasy elements"
                             "\n 1: Hard Boiled Wonderland and the Edge of The World\n 2: Kafka on the Shore"
                             "\n 3: Wild Sheep Chase \n 4: Wind up Bird Chronicle \n 5: Norwegian Wood": 5,
                             "What is the phenomenon called where 'those places ... where all the "
                             "different kinds of truths fit"
                             " together \n"
                             "in Sirens of Titan "
                             "\n 1: Gravimetric vortisphere \n 2: Neomagnonic resonator \n 3: Hyperchronic quasiplexus "
                             "\n 4: Tralfamadorian \n 5: chrono-synclastic infundibulum": 5,
                             "What is the message of The Pearl (John Steinbeck) "
                             "\n 1: Wealth can be a curse\n 2: Love conquers all\n 3: Once bitten twice shy \n 4: "
                             "Don't put"
                             "all your eggs in one basket \n 5: Always be yourself": 1,
                             "Is it ethical to boil lobsters alive according to David Foster Wallace?"
                             "\n 1: Yes \n 2: No": 2,
                             "What is not one of the 12 rules of life, according to Jordan Peterson:"
                             "\n 1: Make friends with people who want the best for you \n 2: Compare "
                             "yourself to who you were "
                             "yesterday, not to who someone else is today. \n 3: Stand up straight "
                             "with your shoulders back. \n"
                             " 4: "
                             "Opportunities don't happen, you create them \n 5: Tell the truth--or, at least, "
                             "don't lie": 4,
                             "In 'Wind up Bird Chronicle', the place the protagonist goes into a different world "
                             "from is:"
                             "\n 1: The ocean \n 2: Under a waterfall  \n 3: A well \n 4: In the basement of his house "
                             "\n 5: In bed, dreaming": 3
                             }

        player_level = inner_character["Knowledge"]
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

    actual_answer = get_question(character)
    try:
        answer = int(input("Choose your answer little one: "))
    except ValueError:
        print("'Please pick a number between 1 and 5 inclusive, you lost 1 HP'")
        character["Current HP"] -= damage_received(character)
    else:
        if answer < 1 or answer > 5:
            print("'You must pick a number between 1 and 5 inclusive, you lost 1 HP'")
            character["Current HP"] -= damage_received(character)
        elif answer == actual_answer:
            character["Current XP"] += 20
            print("You may pass unharmed")
        elif answer != actual_answer:
            print("'Incorrect, 1 hit taken'")
            character["Current HP"] -= damage_received(character)
