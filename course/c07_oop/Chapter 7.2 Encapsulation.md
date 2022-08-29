- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

[go to course contents](https://github.com/ghimiresdp/python-level1/)
<hr>

# Chapter 7.2 Encapsulation

**Table of contents**:

## Introduction

Encapsulation is the process of restricting the direct access to the data.
It can be achieved by binding the private attribute along with methods to make
the data usable. In python we make the data protected by naming the attributes
and methods starting with single underscore`_` or double underscores `__`.

The methods that are bound with protected attributes are called as getters and
setters. the **getter** method takes no arguments and **setter** takes one
argument except `self`.

**Why do we use Getters and Setters instead of public attributes?**

- It helps hiding or prevents modifying the state of the structured data
  preventing the unauthorized access.
- Suppose changing the state of an attribute should affect another attribute,
  the user modifying the public attribute might forget to reflect changes in
  the another.

**example**

```python
class MyClass:
    # protected attribute (accessible from outside of class)
    _name = 'Unknown'

    # private attribute (not accessible from outside of class)
    __age = 20

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age
        # Here, the state of _name is also influenced by the private attribute
        # __age.
        self._name = f'Unknown: {age}'


c1 = MyClass()

# print(c1.__age)
# raises an exception saying no attribute

print()

c1.set_age(30)
# here the age is set to 30 and also the state _name is changed accordingly.

print(c1.get_age())  # 30

# We can access the protected member if it starts with a single _
print(c1._name)  # Unknown: 30
```

**Example 2:** An advanced class representation which takes list of
`Student` objects and changes the state `__is_large` when the number of
students is more than 3

```python
class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __str__(self) -> str:
        return self.name


class ClassRoom:
    def __init__(self, name):
        self.__is_large = False
        self.__students = []
        self.name = name

    def add_student(self, student: Student):  # setter
        self.__students.append(student)
        self.__is_large = True if self.__students.__len__() > 3 else False

    def remove_student(self, student: Student):  # setter / deleter
        if student in self.__students:
            self.__students.remove(student)
            self.__is_large = True if self.__students.__len__() > 3 else False
        else:
            print(f"Student with name {student.name} does not exist")

john = Student("Jon Doe", 1)
py_class = ClassRoom("Python for Beginners")
py_class.add_student(john)
py_class.add_student(Student("John Lennon", 2))
py_class.add_student(Student("John Legend", 3))
py_class.add_student(Student("John Denver", 4))
# here the value __is_large will be set to True

py_class.remove_student(john)
# here the value __is_large will be set to False

```
