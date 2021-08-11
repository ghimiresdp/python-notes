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

"""

# %% example of a class (Animal)
# declaration of class

species_dog = 'dog'
species_man = 'human'


class Animal:
    species = ''  # class attribute (private)
    __legs = 4  # private (accessible only within a class)
    _word = "nothing"  # protected

    # __init__() function
    def __init__(self, name):
        self.name = name  # instance attribute
        pass

    def speak(self):
        print(f'I speak {self._word}')

    def count_legs(self):
        print(f'I have {self.__legs} legs')


# %%
# accessing class attributs
print(Animal.species)  # public
print(Animal._word)  # protected
# print(Animal.__legs)      # unreachable / private

# print(Animal.name)


# %% Instantiating a class
dog = Animal(name="dog")  # dog is an object and Animal is a class
dog.species = 'dog'  # so `dog` is an instance of `Animal`
man = Animal(name='John')
man.species = 'human'

# %% accessing instance attribute
print(dog.name)

# what happens after creating an instance of a class?

# %% __init__() function
