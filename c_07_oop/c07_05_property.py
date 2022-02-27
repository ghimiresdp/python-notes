"""
© https://sudipghimire.com.np


@property decorator in python classes

- They look like regular object variables but are capable of attaching custom behavior to the class.
- They are used as alternative of getters and setters
- whenever we create a property inside a class, it's behavior will be tightly controlled.

for example we want to add a private variable to class and want to access and modify it.
I can achieve it using getter and setter method along with private variable.

or I can add getter, setter and deleter property so that I can access it
similar to attributes rather than calling methods.

structure:
class ABC:

    @property
    def my_property(self):
        # property body
"""

# %%


# Using regular getter and setter
class Student:

    def __init__(self, count: int):
        self.__count = count

    def get_count(self):
        return self.__count

    def set_count(self, value):
        print("I can do other things while updating my value")
        self.__count = value


class_1 = Student(10)
print(class_1.get_count())  # Getter
class_1.set_count(11)
print(class_1.get_count())  # Setter

# %%
# it can be achieved using the property decorator as follows
"""
Getter:
Whenever the getter property is added, the method can be used as the regular variable
we can access this using the regular access method instead of calling the function
eg: value = obj.count


syntax:

@property
def <method_name>(params):
    method body

Whenever the setter property is added, the method can be used as the regular variable and we can assign
the value using regular assignment operator "="

eg: obj.count = 10

syntax:

@<method_name>.setter
def <method_name>(params):
    method body

"""


class Students:

    def __init__(self, count: int):
        self.__count = count

    @property
    def count(self):  # Getter
        return self.__count

    @count.setter  # Setter
    def count(self, value):
        print("I can do other things while updating my value")
        self.__count = value


class_1 = Students(10)
print(class_1.count)
class_1.count = 11
print(class_1.count)

# %%
