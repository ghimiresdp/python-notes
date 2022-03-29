"""
Module Animal

This is a sample module animal which can be imported into different files.
The module contains different constants, variables, functions and classes.
"""
DOMESTIC = 'domestic'
WILD = 'wild'
age = 20


def abc():
    print("Did Something")


class Animal:
    name = ""
    paws = 0
    word = ""

    def __init__(self, name, word):
        self.name = name
        self.word = word

    def __str__(self):
        return (f"Instance of Animal named {self.name}")

    def speak(self):
        print(f'I am {self.name} and I speak with {self.word}s.')

    def rename(self, new_name):
        self.name = new_name


class DomesticAnimal(Animal):
    purpose_of_domestication = ''
