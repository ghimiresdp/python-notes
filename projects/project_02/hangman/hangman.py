import random
import game_data

CONSOLE_WIDTH = 120


class Hangman:
    GUESSES = [
        {
            'word': 'computer',
            'hint': 'An electronic device that is used for storing, and computing data in digital form.'
        },
        {
            'word': 'programming',
            'hint': 'The process of instructing the computer todo certain task.'
        },
        {
            'word': 'inheritance',
            'hint':
            'The process by which a child class takes a base from an another class to retain similar implementation'
        },
        {
            'word': 'polymorphism',
            'hint':
            'The ability of a program in OOP that is able to show different characteristics in different situations'
        },
        {
            'word': 'dictionary',
            'hint': 'A data type in python that has key-value pair'
        },
        {
            'word': 'comprehension',
            'hint': 'A method of generating different collection data types based on another collection of data'
        },
        {
            'word': 'lambda',
            'hint': 'An anonymous function that is used as one liner function'
        },
        {
            'word':
            'iteration',
            'hint':
            'The method of running a sequence of instructions or code in a repeated manned until specific result is achieved'
        },
    ]
    MESSAGES = [
        'We are so excited to have you on our team, {name}!',
        'We are thrilled to have you at our terminal, {name}!',
        'Welcome {name}!! lets start the exciting game',
    ]

    def print_separator(self):
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
        self.username = ''
        self.display_graphics()

    def _randomize(self):
        return NotImplemented

    def play(self):
        self.username = input('Please Enter your Name: ')
        print(self.MESSAGES[random.randrange(0, self.MESSAGES.__len__())].format(name=self.username))
        self.print_separator()


if __name__ == '__main__':
    hangman = Hangman()
    hangman.play()
