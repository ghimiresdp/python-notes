# © https://sudipghimire.com.np
# %%
"""
# Class

- building block of OOP
- we must instantiate an object for a class to perform specific task



## basic Structure

class <ClassName>:
    <attributes>
    <functions>


# Basic Convention

- Class names are in `UpperCamelCase`
    - MyClass
    - ClassOne
    - Animal
- Attributes (variables & methods) are in `snake_case`
- It is better to have 2 vertical spaces before and after classes
- It is better to have a vertical space before and after methods


Class works just like a group or a container for variables and functions

Person
    - first_name
    - last_name
    - address

    - show_fullname()

detailed structure of a class:

class ClassName:
    var1 = <value>
    var2 = <value>

    def function_1(self):
        <function body>

The basics of class includes the following:

- Attributes
    - Class Attributes
    - Instance Attributes
- Methods
    - self parameter

- Instance

- Initializer or constructor    [ __init__() method ]


"""


class Person:
    first_name = ''
    last_name = ''
    address = ''
    city = ''
    age = 0

    def show_fullname(self):
        print(f"{self.first_name} {self.last_name}")


# instantiating the class
mickey = Person()
# what happens after creating an instance of a class?
# discussion in lecture

# Assigning the values to attrobutes
mickey.first_name = "Mickey"
mickey.last_name = "Mouse"
mickey.address = "123 Fantasy Way"
mickey.city = "Anahiem"
mickey.age = 73

# Accessing the values from attributes

print(mickey.first_name)

# calling the methods from the instance
mickey.show_fullname()


# example of a class (Animal) with the __init__() method
class Animal:
    name = ""  # Class Attribute
    paws = 0  # Instance Attribute
    word = ""

    def __init__(self, name, word):
        """
        Constructor or initializer method
        """
        self.name = name
        self.word = word

    def __str__(self):
        return f"Instance of Animal named {self.name}"

    def speak(self):
        print(f'I am {self.name} and I speak with {self.word}s.')

    def rename(self, new_name):
        self.name = new_name


elephant = Animal("John", "trumpet")

elephant.speak()
elephant.rename("Jane")
elephant.speak()

dog = Animal('rockey', 'bark')
dog.speak()

print(dog)
