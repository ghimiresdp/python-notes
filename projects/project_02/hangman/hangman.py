import os
import random
import textwrap
import game_data

CONSOLE_WIDTH = 80


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

    def render_game(self):
        box_width = int(.8 * CONSOLE_WIDTH)
        hint = ' '.join([
            c.center(3, '|' if all(
                (self.__editing, self.__selected_index == idx, c == '_')
            ) else '_' if c == '_' else ' ') for idx, c in
            enumerate(self.progress)
        ])
        self.print_centered("\u2583" * box_width)
        print()
        self.print_centered(
            ' TOTAL ATTEMPTS: {:<10d} CORRECT GUESSES: {:<10d} REMAINING LIVES: {:<10d}'.format(
                self.attempts, self.correct, self.lives
            ).strip().center(box_width)
        )
        print()
        self.print_centered("\u2594" * box_width)
        print()
        for line in textwrap.wrap(self.definition, width=box_width):
            self.print_centered(line)
        print()
        self.print_centered(hint.center(box_width))
        self.print_centered((' '.join([
            (str(idx) if ch == '_' else '').center(3) for idx, ch in enumerate(self.progress)
        ])).center(box_width))
        print()
        print()
        self.print_centered("\u2594" * box_width)
        self.print_centered(
            ' Quit: {:<15s} Select Number: {:<15s} Re-shuffle: {:<15s}'.format(
                'Q', '[NUM]', 'R'
            ).strip().center(box_width)
        )
        self.print_centered("\u2583" * box_width)

    def insert_guess(self, option: str):
        valid = True
        if not option.isnumeric():
            valid = False
        idx = int(option)
        if not self.progress[idx] == '_':
            valid = False
        if not valid:
            print('Invalid options added')
        else:
            self.attempts += 1
            self.__editing = True
            self.__selected_index = idx
            self.render_game()
            value = input('Enter a character to insert: ').upper()
            if value == self.word[idx]:
                self.progress[idx] = value
                self.correct += 1
            else:
                self.lives -= 1
            self.__editing = False
        if '_' not in self.progress:
            print('Congratulations!! You Won the game !!')


class Hangman:
    messages = [
        'We are so excited to have you on our team, {name}!',
        'We are thrilled to have you at our terminal, {name}!',
        'Welcome {name}!! lets start the exciting game',
    ]
    question: Question

    @staticmethod
    def print_centered(value: str):
        print(value.center(CONSOLE_WIDTH))

    def display_graphics(self):
        for line in game_data.graphics:
            for blank, fill in line:
                print(' ' * blank, '\u2588' * fill, end='', sep='')
            print()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __init__(self):
        self.set_random_question()
        self.clear_screen()
        self.display_graphics()
        self.username = input('Please Enter your Name: ')
        self.__editing=False
        self.__selected_index = 0

    def render(self):
        clear_screen = lambda: os.system('cls' if os.name == 'nt' else 'clear')
        clear_screen()
        self.display_graphics()
        hint = ' '.join([
            c.center(3, '|' if all(
                (self.__editing, self.__selected_index == idx, c == '_')) else '_' if c == '_' else ' ')
            for idx, c in enumerate(self.question.progress)
        ])
        self.print_centered("\u2583" * CONSOLE_WIDTH)
        print()
        self.print_centered(' TOTAL ATTEMPTS: {:<10d} CORRECT GUESSES: {:<10d} REMAINING LIVES: {:<10d}'.format(
            self.question.attempts, self.question.correct, self.question.lives).strip().center(CONSOLE_WIDTH))
        print()
        self.print_centered("\u2594" * CONSOLE_WIDTH)
        print()
        for line in textwrap.wrap(self.question.definition, width=CONSOLE_WIDTH):
            self.print_centered(line)
        print()
        self.print_centered(hint.center(CONSOLE_WIDTH))
        self.print_centered((' '.join([(str(idx) if ch == '_' else '').center(3)
                                       for idx, ch in enumerate(self.question.progress)])).center(CONSOLE_WIDTH))
        print()
        print()
        self.print_centered("\u2594" * CONSOLE_WIDTH)
        self.print_centered(' Quit: {:<15s} Select Number: {:<15s} Re-shuffle: {:<15s}'.format(
            'Q', '[NUM]', 'R').strip().center(CONSOLE_WIDTH))
        self.print_centered("\u2583" * CONSOLE_WIDTH)

    def set_random_question(self):
        random_index = random.randrange(0, game_data.questions.__len__())
        self.question = Question(**game_data.questions[random_index])

    def play(self):
        while True:
            self.render()
            option = input("\n\t\tEnter Option: ")
            if option.lower() == 'q':
                break
            elif option.lower() == 'r':
                self.question.randomize_guess()
            else:
                self.question.insert_guess(option)


if __name__ == '__main__':
    hangman = Hangman()
    hangman.play()
