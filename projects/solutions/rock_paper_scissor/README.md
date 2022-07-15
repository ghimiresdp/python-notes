# Project Rock Paper Scissor

The project uses `random` library.
the file `game.py` consists of a class `Game` that does all the gaming logic.

all of the states of the game are defined by instance attributes which are as follows:

1. `username`: Used to save the name of the player.
2. `_consecutive_wins`: Used to track consecutive wins.
3. `last_win`: Used to track who won the last match.
4. `_matches`: Used to count the total number of matches.
5. `_draws`: Used to count total number of draws.
6. `_bot_score`: Used to count the total number of matches won by the bot
7. `_user_score`: Used to count the total number of matches won by the user
8. `user_input`: Used to store the last input of the user
9. `bot_input`: Used to store the last input of the bot

## The `__init__()` method
The `__init__()` function sets the default state whenever initialized.

## The `__get_bot_choice()` method:
This method gives the guess of the bot.

## The `__display_menu()` method:
This method displays the main menu

## Running the game
to run the project, move the terminal to the project folder.

```shell
$ cd projects/project_01/rock_paper_scissor
```
and then run the `game.py` file using the command below:
```shell
$ python game.py
```
