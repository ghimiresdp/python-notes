# © https://sudipghimire.com.np

# %% [markdown]
"""
# Inheritance
- This concept is exactly similar to biological inheritance where child inherits the feature of parent.
- in inheritance, there exists a parent class and child classes which inherits parent's behaviors.
- The base class will be the parent class and the class that is derived from the base class will
  be treated as a child class.

Basic Structure
class Parent:
    <attributes>
    <methods>

class Child(Parent):
    <attributes>
    <methods>


Rectangle
    attributes:
        - width
        - height
    methods:
        - perimeter
        - area
    variants:
        square

Animal
    attributes:
        - legs: 4
        - tail

    variants:
        - Pet
        - Wild
        - Herbivorous
        - Carnivorous

Bank
    attributes:
        - capital
        - interest rate

    variants:
        - branches
        - dev banks
"""


# %% Example Rectangle
class Rectangle:
    width: float = 0
    height: float = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def diagonal_length(self):
        return (self.width ** 2 + self.height ** 2) ** (1 / 2)


# %% child
class Square(Rectangle):

    def __init__(self, width):
        super().__init__(width=width, height=width)

        # del self.area
        # self.width = width
        # self.height = width

    def diagonal_length(self):
        return self.width * (2 ** .5)

    # def area(self):
    #     return None


# %%
room_1 = Rectangle(5, 10)
print(f'Area of room 1: {room_1.area()}')
print(f'Perimeter of room 1: {room_1.perimeter()}')
print(f'Diagonal length of room 1: {room_1.diagonal_length()}')

# %%
room_2 = Square(5)

print(f'Area of room 2: {room_2.area()}')
print(f'Perimeter of room 2: {room_2.perimeter()}')
print(f'Diagonal length of room 2: {room_2.diagonal_length()}')

# %% builtin functions

# isinstance

print(isinstance(room_2, Square))
print(isinstance(room_1, Rectangle))
print(isinstance(room_1, Square))
print(isinstance(room_2, Rectangle))

# %% issubclass

print(issubclass(Square, Rectangle))
print(issubclass(Rectangle, Square))
print(issubclass(Rectangle, object))

# %% monkey patching (generally not recommended)
room_1.name = "My Room"
print(room_1.name)


def print_room_name(self):
    print(self.name)


room_1.print_room_name = print_room_name

room_1.print_room_name(room_1)
