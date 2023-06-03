"""
© https://sudipghimire.com.np

# Class Methods and static methods

Class Methods
- Class methods are special kind of methods that are bound to the class instead of the instance
- If we create an instance and change the property of the object, it is not going to affect the property
  of the classmethod.

Static Methods
- Static methods are methods that do not bind to anything at all and simply return the underlying function
  without any transformation.
- They just behave like a function. Only the difference is they are called along with the class name.
"""


class Animal:
    legs = 4

    @classmethod  # bound to the class so class is passed as the first argument instead of self
    def print_legs(cls):
        print('Total no. of legs: ', cls.legs)

    def print_legs_1(self):  # Regular method that is bound to the instance so self is passed as the first argument
        print('Total no. of legs: ', self.legs)


print(Animal.legs)  # 4

Animal.print_legs()  # 4           # not instantiated
Animal().print_legs()  # 4         # instantiated

human = Animal()
human.legs = 2
human.print_legs()  # 4         # instantiated and attribute is changed but still prints 4 instead of 2

print(human.legs)  # 2

print(Animal.legs)  # 4


# def cm_to_m(value: float):
#     return value/100

# def kg_to_lb(value: float):
#     return value * 2.20462

# cm_value = 3536
# m_value = cm_to_m(cm_value)

# print(m_value)

# wt_kg = 5
# print(kg_to_lb(wt_kg))

# Static Methods
# Just works like a regular function inside the module

class Length:
    cm = 5438

    @staticmethod  # unbound since it does not invoke either of class or an instance.
    def cm_to_m(value: float):
        return value / 100

    @staticmethod
    def m_to_cm(value: float):
        return value * 100


class Weight:
    @staticmethod
    def kg_to_lb(value: float):
        return value * 2.20462

    @staticmethod
    def lb_to_kg(value: float):
        return value / 2.20462


print(Length.cm_to_m(Length.cm))
