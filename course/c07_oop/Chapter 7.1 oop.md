- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

[go to course contents](https://github.com/ghimiresdp/python-level1/)
<hr>

# Chapter 7.1 Object-Oriented Programming (OOP)

**Table of contents**:
- [Chapter 7.1 Object-Oriented Programming (OOP)](#chapter-71-object-oriented-programming-oop)
    - [Introduction to OOP](#introduction-to-oop)
    - [Python Classes](#python-classes)
        - [Attributes, Methods, and the `self` parameter](#attributes-methods-and-the-self-parameter)
        - [The constructor method](#the-constructor-method)
        - [Built-in Class Attributes](#built-in-class-attributes)
        - [Object](#object)


## Introduction to OOP

An Object oriented programming (OOP) is a computer programming model that
organizes the code block around data rather than functions. In functional
programming approach, data and function act as different entity whereas an OOP
approach uses a block of code that contains both data and methods that operate
on those data.

An object-oriented programming covers the limitations of functional programming
by structuring the data and binding the methods to specific object rather than
creating an independent functional block.

**Example 1:**
```python
height = 50
temperature = 90

def add_values(a, b):
    return a + b

print(height + temperature)
```
In the above example, `height` can be added with `temperature` since they both
are integers, but there is no relationship between them so there is no binding
of the function `add_values()` to those data. Furthermore, if we had 2 different
values for height, subtracting one from another would give negative value, which
would also be illogical since there can not be negative height. If we solve the
same problem using and OOP approach, the method would be bound to specific data,
and we could define specific attributes to those data.

### Building blocks of an OOP

An object-oriented programming contains different elements which are as follows:

- **Classes**: Classes are user-defined data types that acts as a blueprint for
  individual objects.
- **Objects**: Objects are instances of a class that contains specific data.
  Generally objects can represent real-world objects such as human, room, etc.
- **Methods**: Methods are functions that are bound to specific objects. For
  example, a `human` object can have `talk` method, whereas a computer object
  can have `boot` method.
- **Attributes**: Attributes are variables that define the property of an object
  Attributes can also be defined as a state of an object for example, if we
  create an object for a `rectangle`, then `length` and `width` will be
  attributes for it.

### Features Of Object-Oriented Programming

An object-oriented programming features those things that can reflect real-world
objects. If we take an example of road-based vehicles, they can be cars, buses,
motorbikes, etc which share some attributes whereas some has different
attributes all of these can be represented with the following:

- Inheritance
- Polymorphism
- encapsulation
- objects
- Data Abstraction

## Python Classes

### Attributes, Methods, and the `self` parameter


### The constructor method

### Built-in Class Attributes

### Object
