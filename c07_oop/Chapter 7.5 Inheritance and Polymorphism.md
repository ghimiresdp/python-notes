- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

[go to course contents](https://github.com/ghimiresdp/python-level1/)
<hr>

# Chapter 7.5: Inheritance and Polymorphism

**Table of contents**:

- [Chapter 7.5: Inheritance and Polymorphism](#chapter-75-inheritance-and-polymorphism)
  - [Introduction to Inheritance](#introduction-to-inheritance)
    - [Types of Inheritance](#types-of-inheritance)


## Introduction to Inheritance

Inheritance is the process of transferring the attributes and behaviors of the
parent class to the child class. This concept is similar to the biological
inheritance where child inherits the feature of parent.

The base class from which all the features are inherited is called the parent
class and the class which inherits parent's features is called a child class.

**Basic Structure of an inheritance:**
```python
class Parent:
    <parent_attributes>
    <parent_methods>

class Child(Parent):
    # here all the parent attributes and methods are automatically inherited to
    # the child class.
    <child_attributes>
    <child_methods>
```
In the above structure, the class `Child` is inherited from the class `Parent`,
hence all the attributes and methods from the class `Parent` is automatically
inherited to the `Child` class.

**Example:**
```python
class Rectangle:
    # parent attributes
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    """
    Here, all the attributes and methods of Rectangle is inherited to the Square
    class.
    """

    # child attributes
    def __init__(self, length):
        # here, Square is also a rectangle which has width same as the length.
        super().__init__(length=length, width=length)
```
In the above example, the class Square do not have any method defined to find
the area, but as it is inherited from the parent class, it is still available
from the class `Rectangle`.

### Types of Inheritance


