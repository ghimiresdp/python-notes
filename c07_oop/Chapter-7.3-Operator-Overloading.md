# Chapter 7.3: Operator Overloading

**Table of contents**:

- [Chapter 7.3: Operator Overloading](#chapter-73-operator-overloading)
  - [Introduction to Operator Overloading](#introduction-to-operator-overloading)
  - [Methods for overloading operations in python](#methods-for-overloading-operations-in-python)
  - [Quick Exercise](#quick-exercise)

## Introduction to Operator Overloading

An operator overloading is the process of making the use of basic arithmetic
operators such as `+`, `-`, etc. to emulate different operations. As the class
objects are not directly mathematically represented, we cannot perform
mathematical operation without instructing the class to do so. The process of
giving the instruction to perform certain mathematical operation can be called
as operator overloading.

We use Magic methods such as `__add__`, `__sub__`, etc to perform overload the
mathematical operations.

The example below explains how two classes can be merged and splited using
mathematical operations:

```python
class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_students(self, *students):
        self.students.extend(students)

    def __add__(self, other):
        new_classroom = ClassRoom(f'{self.name} and {other.name}')
        new_classroom.students = [*self.students, *other.students]
        return new_classroom


c1 = ClassRoom('Python')
c1.add_students('John', 'Jane')

c2 = ClassRoom('Java')
c2.add_students('Mark', 'Satoshi')

c3 = c1 + c2  # This is valid since we have overloaded `+` with `__add__()`

print(c3.name)
# Python and Java
print(c3.students)
# ['John', 'Jane', 'Mark', 'Satoshi']
```

Here, the method `__add__` is responsible for handling the `+` operation. i.e.
whenever 2 `ClassRoom` objects gets added Eg: `c1 + c2`, then it automatically
performs `c1.__add__(c2)` and returns a new instance of `Classroom` with `name`
appended and `students` merged.

## Methods for overloading operations in python

| Symbol | Operator                 | Method                           | Expression  |
|--------|--------------------------|----------------------------------|-------------|
| `+`    | Addition                 | `__add__(self, other)`           | `a1 + a2`   |
| `-`    | Subtraction              | `__sub__(self, other)`           | `a1 - a2`   |
| `*`    | Multiplication           | `__mul__(self, other)`           | `a1 * a2`   |
| `/`    | Division                 | `__div__(self, other)`           | `a1 / a2`   |
| `//`   | Floor Division           | `__floordiv__(self, other)`      | `a1 // a2`  |
| `%`    | Modulo/Remainder         | `__mod__(self, other)`           | `a1 % a2`   |
| `**`   | Power                    | `__pow__(self, other[, modulo])` | `a1 ** a2`  |
| `<<`   | Bitwise Left Shift       | `__lshift__(self, other)`        | `a1 << a2`  |
| `>>`   | Bitwise Right Shift      | `__rshift__(self, other)`        | `a1 >> a2`  |
| `&`    | Bitwise AND              | `__and__(self, other)`           | `a1 & a2`   |
| `^`    | Bitwise XOR              | `__xor__(self, other)`           | `a1 ^ a2`   |
| `\|`   | (Bitwise OR)             | `__or__(self, other)`            | `a1 \| a2`  |
| `-`    | Negation (Arithmetic)    | `__neg__(self)`                  | `-a1`       |
| `+`    | Positive                 | `__pos__(self)`                  | `+a1`       |
| `~`    | Bitwise NOT              | `__invert__(self)`               | `~a1`       |
| `<`    | Less than                | `__lt__(self, other)`            | `a1 < a2`   |
| `<=`   | Less than or Equal to    | `__le__(self, other)`            | `a1 <= a2`  |
| `==`   | Equal to                 | `__eq__(self, other)`            | `a1 == a2`  |
| `!=`   | Not Equal to             | `__ne__(self, other)`            | `a1 != a2`  |
| `>`    | Greater than             | `__gt__(self, other)`            | `a1 > a2`   |
| `>=`   | Greater than or Equal to | `__ge__(self, other)`            | `a1 >= a2`  |
| `[1]`  | Index operator           | `__getitem__(self, index)`       | `a1[index]` |
| `in`   | In operator              | `__contains__(self, other)`      | `a2 in a1`  |

> **Note:** If the bitwise OR `|` operation rendered as `\|` in the above table
> then please remember that the same pipe operator `|` is used as a table column
> separator in markdown files. Hence it is escaped using `\|`.
> But the actual operation should be written in format `a | b` but not `a \| b`.

## Quick Exercise

Create a class named `Line` and add the attribute `length` to it. Now create a
method that overloads the addition operation. the operation should return the
new `Line` instance with added length into it.

```python
class Line:
    def __init__(self, length):
        self.length = length

    # add your method here



    # end of your answer


l1 = Line(5)
l2 = Line(10)

l3 = l1 + l2
print(type(l3))     # It should print `<class `__main__.Line`>`
print(l3.length)    # It should print `15`
```
