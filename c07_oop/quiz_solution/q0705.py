"""
© https://sudipghimire.com.np

create a classes Rectangle, Circle and Box and add respective attributes eg.: radius, length, width, height

for Rectangle, create methods to find out:
    perimeter
    area
    length of diagonal

for Circle, create methods to find out:
    circumference
    area
    diameter

for Box, create methods to find out:
    surface area
    volume
"""

# answer

class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def diagonal_length(self):
        return (self.width**2 * self.height**2)**0.5


class Circle:
    __PI = 3.1415

    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return self.__PI * self.radius**2

    def diameter(self):
        return 2 * self.radius

    def circumference(self):
        return self.diameter() * self.__PI
        # return 2 * self.radius * self.__PI    # This solution also works


class Box:
    def __init__(self, length, width, height) -> None:
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self):
        return 2 * (self.length * self.width + self.width * self.height + self.length * self.height)

    def volume(self):
        return self.length * self.width + self.height


# tests

rect1 = Rectangle(5, 6)
print('Area of rectangle:', rect1.area())
print('Perimeter of rectangle:', rect1.perimeter())
print('Length of diagonal:', rect1.diagonal_length())
print()

circle = Circle(10)
print('Area of Circle:', circle.area())
print('Perimeter of Circle:', circle.circumference())
print('Diameter of Circle:', circle.diameter())
print()

box1 = Box(5, 6, 7)
print('Surface Area of Box:', box1.surface_area())
print('Volume of the box:', box1.volume())
print()
