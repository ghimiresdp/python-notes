"""
© https://sudipghimire.com.np

Encapsulation

- It is the process of restricting the direct access to the data.
- Encapsulation is achieved by binding the data along with methods to make the data usable.
- When the attribute becomes private, we do not have direct access to the data that time we use
  getters and setters to retrieve and set the value to the variable.

Encapsulation in Python.

Encapsulation can be achieved using the following methodologies in python:
1. Getters and Setters
2. Property
"""
# Getters and Setters
"""
- whenever we need to access private attributes, we need to create the helper function that has access to those
  attributes. The helper functions can get or set values of the attribute.
- getter generally takes no parameter and setter takes at least one parameter


Why do we use Getters and setters instead of public variables?

- It helps achieving encapsulation which helps hiding or modifying the state of the structured data
  preventing the unauthorized access.
- Suppose changing the state of an object should change another attributes and if we give them accessing the state,
  then the program should behave abnormally.
- It helps avoiding mistakes when we want to change the state when we want to change states repeatedly.

"""


class MyClass:
    __value = 1

    def get_value(self):  # Getter method
        return self.__value

    def set_value(self, value):  # Setter Method
        self.__value = value


cls1 = MyClass()
cls1.set_value(5)
print(cls1.get_value())
"""
An advanced Example: ClassRoom of students
"""
MALE = 'male'
FEMALE = 'female'


class Student:

    def __init__(self, name, roll, gender):
        self.name = name
        self.roll = roll
        self.gender = gender

    def __str__(self) -> str:
        return f"{self.roll}\t{self.name}"


class ClassRoom:

    def __init__(self, name, class_teacher):
        self.__is_large = False
        self.__students = []
        self.name = name
        self.class_teacher = class_teacher

    def add_student(self, student: Student):
        print('[ Adding Student ]'.center(80, '='))
        self.__students.append(student)
        if self.__students.__len__() > 3:
            self.__is_large = True
        else:
            self.__is_large = False

    def remove_student(self, student: Student):
        print('[ Removing Student ]'.center(80, '='))
        if student in self.__students:
            self.__students.remove(student)
            if self.__students.__len__() > 3:
                self.__is_large = True
            else:
                self.__is_large = False
        else:
            print(f"Student with name {student.name} does not exist")

    def describe(self):
        print("Students")
        for student in self.__students:
            print(student)
        print("Large: ", self.__is_large)


py_class = ClassRoom("Python for Beginners", "Sudip Ghimire")

jon = Student("Jon Doe", 1, MALE)

py_class.add_student(jon)
py_class.add_student(Student("Jane Doe", 2, FEMALE))

py_class.describe()
