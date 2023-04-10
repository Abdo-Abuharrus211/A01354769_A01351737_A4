# COMP1510-Assignment 4

Create a text based game to impress Chris and win a GOTY award!<br>
Written in Python, of course.

## Team members' names:

KATE SULLIVAN

ABDULQADIR ABUHARRUS

## Team members' student numbers:

KS: A01354769

AA: A01351737

## Your GitHub account ID:

katesully

Abdo-Abuharrus211

## Comments & Declarations:

We're going to make a game to rule all games!

## Narrative:

Welcome to the Cata game! In this game, you play as a caterpillar in a dusty
bookstore in a small town. You will explore the bizarre landscape of the library, encounter friendly inhabitants who 
will inform you of the land and your quest, and face foes such as ants, spiders, mice, cats, and even the mighty 
Python of the Courtyard!
## Gameplay

You start as a caterpillar that doesn't know where it is or who....
You stumble upon some scrolls etched with strange symbols resembling compass points, gaining +20 XP.
You set out on a trek through the bizarre landscape of the library, traversing books, scrolls, dusty shelves,
exotic carpets, and desks cluttered with receipts and spilled coffee.
Each location in the 10x10 grid has a unique description.
Along the way, you encounter friendly inhabitants who aid your quest, but also face foes such as ants, spiders,
mice, cats, and even the mighty Python of the Courtyard!
To earn the rite of passage and ascend, you must face the Python and answer its final questions.

## Setting

The game takes place in a dusty, rustic, and homey bookstore in a small town.
The cozy garden behind the bookshop has a fountain, arbors, ferns, flowering shrubs, grasses, and a koi pond.
Beneath the fair Lemon Tree lies the Python, once a beloved pet but now the tyrant of the bookshop dominion, clutching 
it with an iron coil. None dare challenge it!


---

## Assignment Requirements

| Requirement                       | Location                                                  |
|-----------------------------------|-----------------------------------------------------------|
| game.pdf                          | In root directory                                         |
| game.py                           | Module in root directory                                  |
| 10x10 grid                        | game.py -> game() -> L 25 & L 26                          |
| Character with attributes         | assets.py -> make_character() ->L 123                     |
| Char movement in 4 directions     | game_mechanics.py -> move_character() -> L 49             |
| Chance encounter                  | game_state_control.py -> check_for_foe() -> L 64          |
| Char overcome obstacle/foe        | guessing_game.py -> guessing_game() -> L 7                |
| Game end after final boss         | game_user_io.py -> final_boss() -> L 44                   |
| Char start at level 1 ("Novice")  | assets.py -> make_character() ->L 123                     |
| Named levels                      | game_state_control.py -> level_up() -> L 146              |
| Char damage resistance gain       | game_state_control.py -> damage_received() -> L 108       |
| Final boss at level 3             | game_state_control.py -> check_for_final_boss() -> L 189  |
| Variety of tricky  questions      | guessing_game.py -> guessing_game() -> L 39               |
| Char dies when HP is zero         | game_state_control.py -> dead_yet() ->  L 76              |
| Tuples for room descriptions      | assets.py -> line 19                                      |
| Dictionaries for Character        | assets.py -> make_character() -> L 133                    |
| Exceptions...Everywhere....       | game.py -> game() -> L 50                                 |
| Organized modules                 | check game directories structure                          |
| If statements                     | load_or_new_game.py -> load_char_or_new() -> L 19         |
| Comprehensions                    | assets.py -> L 116                                        |
| Looping                           | game.py -> game() -> L 37                                 |
| Membership operator               | game_state_control.py -> L 208                            |
| Range function                    | assets.py -> L 116                                        |
| Itertools functions               | assets.py -> L 116                                        |
| The Random module                 | guessing_game.py -> L 136                                 |
| Function annotations              | See test modules for @patch                               |
| Doctests and Docstrings           | Every function as deemed appropriate                      |
| Formatted outputs using F-Strings | All print statements for example, game_user_io.py -> L 36 |




