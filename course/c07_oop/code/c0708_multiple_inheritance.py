"""
© https://sudipghimire.com.np

Multiple Inheritance.

Multiple inheritance means inheriting the behavior from 2 or more parent classes.

The structure would be

class A:
    <attributes>
    <methods>

class B:
    <attributes>
    <methods>

classs C(A, B):
    <attributes>
    <methods>

- In multiple inheritance, Python uses C3 Linearization algorithm to determine the order in which
  to resolve class attributes and methods. The process is also known as Method Resolution Order (MRO)

  To learn more about C3 linearization, you can check the link below:
  https://en.wikipedia.org/wiki/C3_linearization

"""


class Parent1:
    x = 5


class Parent2:
    x = 10


class Child(Parent1, Parent2):  # According to C3 linearization, Child accepts x from Parent1.
    pass


child = Child()

print(child.x)


class Shop:
    def __init__(self) -> None:
        self.__reg_no=0

    def get_reg_no(self):
        return self.__reg_no

    def set_reg_no(self, value):
        self.__reg_no = value



class CoffeeShop(Shop):
    coffee_price = 30


class Bakery(Shop):
    dough_nut_price = 10


class Restaurant(CoffeeShop, Bakery):
    pizza_price = 20

    def __init__(self, reg_no) -> None:
        super().__init__()
        self.set_reg_no(reg_no)


r1 = Restaurant('A12345')

r1.dough_nut_price = 15

print(r1.get_reg_no())
print(r1.dough_nut_price)
print(r1.coffee_price)
print(r1.pizza_price)

print(isinstance(r1, Restaurant))
print(isinstance(r1, Bakery))
print(isinstance(r1, CoffeeShop))
print(isinstance(r1, Shop))
