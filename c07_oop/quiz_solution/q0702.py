"""
© https://sudipghimire.com.np

Create a class named Person and add the following attributes and methods:
    - name:     Instance attribute
    - age:      Instance attribute
    - gender:   Instance attribute
    - weight:   Class attribute

    - year_of_birth():
        Returns the year by subtracting the age from the current year.

    - get_pronouns():
        Returns list of ['he', 'his', 'him'] or ['she', 'her', 'hers'] by checking the gender

    the initializer method should take name, age, and gender
"""

import datetime
from ntpath import join

# answer
MALE = 'male'
FEMLALE = 'female'

class Person:

    weight = 0

    def __init__(self, name: str, age: int, gender: str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def year_of_birth(self):
        return datetime.date.today().year - self.age

    def get_pronouns(self):
        return ['he', 'his', 'him'] if self.gender == MALE else ['she', 'her', 'hers']
        # you can also accept other, unspecified option to gender for practice



# Test
john = Person("John Doe", 20, MALE)

print(john.year_of_birth())
print(john.get_pronouns())
