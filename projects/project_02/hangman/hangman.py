import random

import game_data

CONSOLE_WIDTH = 120


class Question:
    def __init__(self, word: str, definition: str):
        self.word = word.upper()
        self.definition = definition
        hints = sorted(random.sample(range(word.__len__()), k=word.__len__() // 3 + 1))
        self.progress = [char if idx in hints else '_' for idx, char in enumerate(list(self.word))]
        self.lives = self.word.__len__() - hints.__len__()
        self.attempts = 0
        self.correct = 0

    @staticmethod
    def print_centered(value: str):
        print(value.center(CONSOLE_WIDTH))

    def display_progress(self, display_index=True):
        box_width = int(.8 * CONSOLE_WIDTH)
        self.print_centered(f'+{"-" * box_width}+')
        self.print_centered(
            '|'+' TOTAL ATTEMPTS: {:<10d} CORRECT GUESSES: {:<10d} REMAINING LIVES: {:<10d}'.format(
                self.attempts, self.correct, self.lives
            ).strip().center(box_width)+'|'
        )
        self.print_centered(f'+{"-" * box_width}+')
        self.print_centered(f'|{" " * box_width}|')
        self.print_centered(f'|{" ".join(self.progress).center(box_width)}|')
        self.print_centered(f'|{" " * box_width}|')
        self.print_centered(f'+{"-" * box_width}+')


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
        self.print_separator()
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
        self.question.display_progress()


if __name__ == '__main__':
    hangman = Hangman()
    hangman.play()
