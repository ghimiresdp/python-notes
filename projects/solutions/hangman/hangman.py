import os
import random
import textwrap
from typing import Tuple
from game_data import WINNER, LOOSER, HANGMAN

CONSOLE_WIDTH = 80


class Question:

    def __init__(self, word: str, definition: str):
        self.word = word.upper()
        self.definition = definition
        self.__progress = sorted(random.sample(range(word.__len__()), k=(2 * word.__len__()) // 3))

    @property
    def remaining(self):
        return self.__progress

    @property
    def hints(self):
        return (['_' if idx in self.remaining else char for idx, char in enumerate(list(self.word))])

    def insert_guess(self, value: str) -> Tuple[bool, bool]:
        """
        Returns 2 values (correct: `bool`, changed: `bool`)
        """
        value = value.upper()
        changed = False
        for idx in self.__progress:
            if self.word[idx] == (value):
                changed = True
                self.__progress.remove(idx)
        return True if value in self.word else False, changed


class Hangman:
    messages = [
        'We are so excited to have you on our team, {name}!',
        'We are thrilled to have you at our terminal, {name}!',
        'Welcome {name}!! lets start the exciting game',
    ]
    questions = [
        {
            'word': 'computer',
            'definition': 'An electronic device that is used for storing, and computing data in digital form.'
        },
        {
            'word': 'programming',
            'definition': 'The process of instructing the computer todo certain task.'
        },
        {
            'word':
            'inheritance',
            'definition':
            'The process by which a child class takes a base from an another class to retain similar implementation'
        },
        {
            'word':
            'polymorphism',
            'definition':
            'The ability of a program in OOP that is able to show different characteristics in different situations'
        },
        {
            'word': 'dictionary',
            'definition': 'A data type in python that has key-value pair'
        },
        {
            'word': 'comprehension',
            'definition': 'A method of generating different collection data types based on another collection of data'
        },
        {
            'word': 'lambda',
            'definition': 'An anonymous function that is used as one liner function'
        },
        {
            'word':
            'iteration',
            'definition':
            'The method of running a sequence of instructions or code in a repeated manner '
            'until specific result is achieved'
        },
    ]
    question: Question

    def __init__(self):
        self.set_random_question()
        self.__lives = 3
        self.__attempts = 0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def render(self):
        hint = ' '.join([c.center(3, '_' if c == '_' else ' ') for idx, c in enumerate(self.question.hints)])
        print("=" * CONSOLE_WIDTH)
        print(f' TOTAL ATTEMPTS: {self.__attempts:<10d} REMAINING LIVES: {self.__lives:<10d}'.strip().center(
            CONSOLE_WIDTH))
        print("-" * CONSOLE_WIDTH, end='\n\n')
        for line in textwrap.wrap(self.question.definition, width=CONSOLE_WIDTH):
            print(line.center(CONSOLE_WIDTH))
        print()
        print(hint.center(CONSOLE_WIDTH), end='\n\n')
        print("-" * CONSOLE_WIDTH)
        print(f'Shuffle Questions: {1:<5d}Quit : 0'.center(CONSOLE_WIDTH))
        print("=" * CONSOLE_WIDTH)

    def set_random_question(self):
        random_index = random.randrange(0, self.questions.__len__())
        question = Question(**self.questions[random_index])
        self.question = question

    def play(self):
        while True:
            self.clear_screen()
            print(LOOSER if self.__lives == 0 else WINNER if self.question.remaining.__len__() == 0 else HANGMAN)

            self.render()
            option = input("Enter Option [0 / 1 / a-z]: ".rjust(CONSOLE_WIDTH // 2))
            if option == '0':
                print("See you Again!!".center(CONSOLE_WIDTH))
                break
            elif option == '1':
                self.__init__()
            else:
                if self.question.remaining.__len__()>0:
                    correct, changed = self.question.insert_guess(option)
                    if changed:
                        self.__attempts += 1
                    if not correct:
                        self.__lives -= 1


if __name__ == '__main__':
    hangman = Hangman()
    hangman.play()
