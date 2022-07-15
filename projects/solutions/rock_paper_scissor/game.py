from random import random

import random

BOX_WIDTH = 60  # width of the box to show in the stats bar


class Game:
    # Menu items to display when game starts
    __menu = {
        1: {
            'name': 'ROCK',
            'symbol': '👊'
        },
        2: {
            'name': 'PAPER',
            'symbol': '🤚'
        },
        3: {
            'name': 'SCISSOR',
            'symbol': '✌️'
        },
        0: {
            'name': 'Restart Game',
            'symbol': '🔂'
        },
        9: {
            'name': 'Quit Game',
            'symbol': '🔄'
        },
    }

    def __init__(self, username):
        self.username = username
        self._consecutive_wins = 0  # counter for consecutive wins
        self.last_win = False  # true if user wins

        self._matches = 0
        self._draws = 0
        self._bot_score = 0
        self._user_score = 0
        self._user_input = 0
        self._bot_input = 0

    def __get_bot_choice(self):
        return random.randint(1, 3)

    def __display_menu(self) -> bool:
        print()
        for id, item in self.__menu.items():
            print(f"{id}. [{item['symbol']}] {item['name']}")
        try:
            option = int(input("ROCK-PAPER-SCISSOR [Select an option to continue]: "))
            self.__menu[option]
            self._user_input = option
            self._bot_input = self.__get_bot_choice()
            return True
        except (KeyError, ValueError):
            print('\n', "[ invalid option supplied ]".center(BOX_WIDTH + 2, '='), end='')
            return False

    def inner_stats(self, text: str, value, end=''):
        print('|  ', text.ljust(BOX_WIDTH // 2 - 15), f'{value}'.rjust(10), '  |', sep='', end=end)

    def stats(self, remarks: str):
        print('\n', '+', '[ GAME STATISTICS ]'.center(BOX_WIDTH, '-'), '+', sep='')

        self.inner_stats(self.username, self.__menu[self._user_input]['name'])
        self.inner_stats('Bot', self.__menu[self._bot_input]['name'], end='\n')

        self.inner_stats('Total Rounds', self._matches)
        self.inner_stats('Total Draws', self._draws, end='\n')

        self.inner_stats(self.username, self._user_score)
        self.inner_stats('Bot', self._bot_score, end='\n')

        print('+', f'[ {remarks} ]'.center(BOX_WIDTH, '-'), '+', sep='')

    def evaluate(self):
        self._matches += 1
        if self._user_input == self._bot_input:
            self._draws += 1
            return 'DRAW'
        elif (self._user_input, self._bot_input) in ((1, 3), (2, 1), (3, 2)):
            self._user_score += 1
            if self.last_win:
                self._consecutive_wins += 1  # consecutive wins value will be added by 1
            else:
                self.last_win = True  # reset the last winner to User
                self._consecutive_wins = 1
            return f'{self.username.upper()} WINS'
        else:
            self._bot_score += 1
            if self.last_win:
                self.last_win = False  # reset the last winner to Bot
                self._consecutive_wins = 1
            else:
                self._consecutive_wins += 1  # consecutive wins value will be added by 1
            return f'BOT WINS'

    def play(self):
        while True:
            if not self.__display_menu():
                continue
            if self._user_input == 9:
                print("Nice Playing with you, Good Bye !!")
                return
            elif self._user_input == 0:
                print('[ Restarting the game ]'.center(BOX_WIDTH + 2, '='))
                self._matches = 0
                self._draws = 0
                self._bot_score = 0
                self._user_score = 0
                self._user_input = 0
                self._bot_input = 0
                # self.stats('Restarting the game')
                continue
            message = self.evaluate()
            self.stats(message)
            if self._consecutive_wins == 3:
                print(f'[ 3 Consecutive wins by {self.username if self.last_win else "BOT"} ]'.center(
                    BOX_WIDTH + 2, '='))
                break


print("[ ROCK PAPER SCISSOR ]".center(BOX_WIDTH + 2, '='))
name = input('\nPlease enter your name to continue: ')
game = Game(name)
game.play()
