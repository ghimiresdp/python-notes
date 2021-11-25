"""
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


class Students:
    def __init__(self, count: int):
        self.__count = count

    def get_count(self):
        return self.__count

    def set_count(self, value):
        print("I can do other things while updating my value")
        self.__count = value


class_1 = Students(10)
print(class_1.get_count())
class_1.set_count(11)
print(class_1.get_count())


# %%
# it can be achieved using the property decorator as follows
class Students:
    def __init__(self, count:int):
        self.__count = count

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        print("I can do other things while updating my value")
        self.__count = value


class_1 = Students(10)
print(class_1.count)
class_1.count = 11
print(class_1.count)

# %%
