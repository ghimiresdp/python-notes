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
"""


# %% Example Rectangle
class Rectangle:  # Parent Class

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def diagonal_length(self):
        return (self.width ** 2 + self.height ** 2) ** (1 / 2)


# Child Class
class Square(Rectangle):  # Here, the class `Square` is inheriting all the properties from the class `Rectangle`.

    def __init__(self, width):
        super().__init__(width=width, height=width)  # in python3, super() does not require any arguments

    def diagonal_length(self):
        return self.width * (2 ** .5)


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

# %% builtin functions that work with inheritance
"""
isinstance()
the method returns True if an object is the instance of the class ir any of the derived classes of a class

"""


class Parent:
    pass


class Child(Parent):
    pass


obj1 = Parent()
obj2 = Child()
"""
here,
- obj1 is an instance of a class Parent
- obj2 is an instance of a class Child

Note:
- instance of a parent class is not an instance of a child class
- instance of a child class is also an instance of a parent class since it is inherited from a parent class
"""

print(isinstance(room_2, Square))
print(isinstance(room_1, Rectangle))
print(isinstance(room_1, Square))
print(isinstance(room_2, Rectangle))
"""
issubclass()
the method returns True if the derived class is the subclass of the base class.
"""

print(issubclass(Square, Rectangle))
print(issubclass(Rectangle, Square))
print(issubclass(Rectangle, object))
