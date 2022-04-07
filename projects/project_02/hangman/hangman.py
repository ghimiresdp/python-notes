import os
import random

import game_data

CONSOLE_WIDTH = 120


class Question:
    __editing = False
    __selected_index = 0

    def __init__(self, word: str, definition: str):
        self.word = word.upper()
        self.definition = definition
        self.attempts = 0
        self.correct = 0
        self.lives = 0
        self.progress = []
        self.randomize_guess()

    @staticmethod
    def print_centered(value: str):
        print(value.center(CONSOLE_WIDTH))

    def randomize_guess(self):
        hints = sorted(random.sample(range(self.word.__len__()), k=self.word.__len__() // 3 + 1))
        self.progress = [char if idx in hints else '_' for idx, char in enumerate(list(self.word))]
        self.lives = self.word.__len__() - hints.__len__()
        self.attempts = 0
        self.correct = 0

    def display_game_screen(self):
        clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')
        clear_screen()
        box_width = int(.8 * CONSOLE_WIDTH)
        hint = ' '.join([
            c.center(3, '|' if all(
                (self.__editing, self.__selected_index == idx, c == '_')
            ) else '_' if c == '_' else ' ') for idx, c in
            enumerate(self.progress)
        ])
        self.print_centered(f'+{"-" * box_width}+')
        self.print_centered(
            '|' + ' TOTAL ATTEMPTS: {:<10d} CORRECT GUESSES: {:<10d} REMAINING LIVES: {:<10d}'.format(
                self.attempts, self.correct, self.lives
            ).strip().center(box_width) + '|'
        )
        self.print_centered(f'+{"-" * box_width}+')
        self.print_centered(f'|{" " * box_width}|')
        self.print_centered(f'|{hint.center(box_width)}|')
        self.print_centered('|' + (' '.join([
            (str(idx) if ch == '_' else '').center(3) for idx, ch in enumerate(self.progress)
        ])).center(box_width) + '|')
        self.print_centered(f'|{" " * box_width}|')
        self.print_centered(f'+{"-" * box_width}+')
        self.print_centered(
            '|' + ' Quit: {:<15s} Select Number: {:<15s} Re-shuffle: {:<15s}'.format(
                'Q', '[NUM]', 'R'
            ).strip().center(box_width) + '|'
        )
        self.print_centered(f'+{"-" * box_width}+')

    def insert_guess(self, option: str):
        valid = True
        if option.isnumeric():
            idx = int(option)
            if self.progress[idx] == '_':
                self.__editing = True
                self.display_game_screen()
                value = input('Enter a character to insert: ')
        if not valid:
            print('Invalid options added')


class Hangman:
    messages = [
        'We are so excited to have you on our team, {name}!',
        'We are thrilled to have you at our terminal, {name}!',
        'Welcome {name}!! lets start the exciting game',
    ]
    question: Question = None

    @staticmethod
    def print_separator():
        print('=' * CONSOLE_WIDTH)

    def display_graphics(self):
        for line in game_data.GRAPHICS:
            for blank, fill in line:
                print(' ' * blank, '/' * fill, end='', sep='')
            print()

        print('\n'.join(''))
        self.print_separator()

    def __init__(self):
        self.display_graphics()
        self.username = input('Please Enter your Name: ')
        print(self.messages[random.randrange(0, self.messages.__len__())].format(name=self.username))
        self.print_separator()

    def play(self):
        random_index = random.randrange(0, game_data.questions.__len__())
        self.question = Question(**game_data.questions[random_index])
        while True:
            print(self.question.definition)
            print("Guess the answer:")
            self.question.display_game_screen()
            option = input("\n\t\tEnter Option: ")
            if option.lower() == 'q':
                break
            elif option.lower() == 'r':
                self.question.randomize_guess()
                self.question.display_game_screen()
            else:
                self.question.insert_guess(option)


if __name__ == '__main__':
    hangman = Hangman()
    hangman.play()
