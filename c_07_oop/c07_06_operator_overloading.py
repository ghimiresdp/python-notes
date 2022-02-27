"""
© https://sudipghimire.com.np


Operator Overloading

- it is the process of overloading the basic operators such as +, -, *, /, etc.
- we can perform calculations between instances with the help of operator overloading

Below are the magic methods that will overload expressions between similar instance of classes.


Symbol  Operator                          Method                            Expression
--------------------------------------------------------------------------------------------------
+       Addition                        __add__(self, other)                a1 + a2
-       Subtraction                     __sub__(self, other)                a1 - a2
*       Multiplication                  __mul__(self, other)                a1 * a2
/       Division                        __div__(self, other)                a1 / a2
//      Floor Division                  __floordiv__(self, other)           a1 // a2
%       Modulo/Remainder                __mod__(self, other)                a1 % a2
**      Power                           __pow__(self, other[, modulo])      a1 ** a2
<<      Bitwise Left Shift              __lshift__(self, other)             a1 << a2
>>      Bitwise Right Shift             __rshift__(self, other)             a1 >> a2
&       Bitwise AND                     __and__(self, other)                a1 & a2
^       Bitwise XOR                     __xor__(self, other)                a1 ^ a2
|       (Bitwise OR)                    __or__(self, other)                 a1 | a2
-       Negation (Arithmetic)           __neg__(self)                       -a1
+       Positive                        __pos__(self)                       +a1
~       Bitwise NOT                     __invert__(self)                    ~a1
<       Less than                       __lt__(self, other)                 a1 < a2
<=      Less than or Equal to           __le__(self, other)                 a1 <= a2
==      Equal to                        __eq__(self, other)                 a1 == a2
!=      Not Equal to                    __ne__(self, other)                 a1 != a2
>       Greater than                    __gt__(self, other)                 a1 > a2
>=      Greater than or Equal to        __ge__(self, other)                 a1 >= a2
[1]     Index operator                  __getitem__(self, index)            a1[index]
in      In operator                     __contains__(self, other)           a2 in a1

"""
"""
Example, we have a class for a classroom.

classroom "Python Class" has total of 5 students
classroom "Java Class" has total of 5 students

we want to merge the classes which should now have total 10 students.

In this case we can perform operator overloading in the class definition so that we can easily use + operator
"""

from typing import List

MALE = 'male'
FEMALE = 'female'


class Student:

    def __init__(self, name, roll, gender):
        self.name = name
        self.roll = roll
        self.gender = gender

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.__str__()


class ClassRoom:

    def __init__(self, name) -> None:
        self.name = name
        self.students: List[Student] = []

    def __add__(self, other: "ClassRoom"):
        """
        this method overrides `+` operator so thatwe can use
        a + b where a and b are instances of the class `ClassRoom`.
        The method finally returns the result where the name and students will be merged.
        """
        result = ClassRoom(f"{self.name}_{other.name}")
        result.students = [*self.students, *other.students]
        return result


py_class = ClassRoom("Python")
py_class.students.append(Student("John", 1, MALE))
py_class.students.append(Student("Jane", 2, FEMALE))

java_class = ClassRoom("Java")
java_class.students.append(Student('Donald', 3, MALE))
java_class.students.append(Student('Diana', 4, FEMALE))

print(py_class.students)  # [John, Jane]
print(java_class.students)  # [Donald, Diana]

merged = py_class + java_class  # [John, Jane, Donald, Diana]

print(merged.name)

print(merged.students)
