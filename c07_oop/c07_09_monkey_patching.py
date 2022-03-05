"""
© https://sudipghimire.com.np

Monkey Patching

- it is the process of adding new variable or method to a class after it's been defined
- we can introduce a new instance attribute to an object even after it has been initialized
- monkey patching is useful when we do not want to perform inheritance or create a child class and
  change the behavior of the previously defined classes or previously instantianted objects.

- if we monkey patch the instance attribute, it is not going to change the class template, instead
  it affects only the instance we've created
"""


class Student:
    def __init__(self, name):
        self.name = name

Student.grade = 1  # Monkey Patching Class attribute
Student.major = 'science'
john = Student("John Doe")

print(john.name)
john.roll = 5  # Monkey Patching instance attribute
print(john.roll)


def display_name(self):
    print(self.name)


def display_major(self):
    print(self.major)


Student.display_name = display_name  # Monkey patching class attribute
Student.display_major = display_major

john.display_name()


jane = Student("Jane")
print(jane.roll)
