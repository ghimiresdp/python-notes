- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

[go to course contents](https://github.com/ghimiresdp/python-level1/)
<hr>

# Chapter 7.1 Object-Oriented Programming (OOP)

**Table of contents**:
- [Chapter 7.1 Object-Oriented Programming (OOP)](#chapter-71-object-oriented-programming-oop)
    - [Introduction to OOP](#introduction-to-oop)
        - [Building blocks of an OOP](#building-blocks-of-an-oop)
        - [Features Of Object-Oriented Programming](#features-of-object-oriented-programming)
    - [Python Classes](#python-classes)
        - [PEP-8 Conventions for creating a class](#pep-8-conventions-for-creating-a-class)
    - [Basic Building block of Classes](#basic-building-block-of-classes)
        - [Attributes, Methods, and the `self` parameter](#attributes-methods-and-the-self-parameter)
        - [Initializing the class, Constructor Method, and uses of `self`.](#initializing-the-class-constructor-method-and-uses-of-self)
        - [Class Attributes and Instance attributes](#class-attributes-and-instance-attributes)
        - [Built-in Class Attributes](#built-in-class-attributes)
        - [Object](#object)
    - [In python, everything are objects](#in-python-everything-are-objects)


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

Python classes can be created using a `class` keyword.

**Basic Structure of a class**
```python
class ClassName:
    attr_1 = value
    attr_2 = value

    def method_1(self):
        function body
```

### PEP-8 Conventions for creating a class

- class names should be written in `UpperCamelCase`.
- class attributes and methods should be written in `snake_case`.
- We should separate classes with 2 blank lines and methods with a blank line.

**Example:**
```python
class Person:
    first_name = ''
    last_name = ''

    def show_full_name(self):
        return f'{self.first_name} {self.last_name}'
```

The above example uses `first_name` and `last_name` as attributes of the class
`Person` whereas `show_full_name()` as the method that binds to the person

## Basic Building block of Classes

Classes are made up of the following building blocks:

- Attributes
    - Class Attribute
    - Instance Attribute
- Methods
    - Class Methods
    - Static Methods
    - initializer method
- Instance


### Attributes, Methods, and the `self` parameter

- All the variables defined inside a class are attributes.
- Attribute acts as a state of the class which changes over time and condition
- All functions defined inside a class are known as methods
- All instance methods use the first parameter `self` which references the
  instance itself.

```python
class Person:
    first_name = '' # Attribute
    last_name = ''

    def show_fullname(self):    # method
        print(f"{self.first_name} {self.last_name}")
```

### Initializing the class, Constructor Method, and uses of `self`.

The constructor method is a method that initializes the class. in python,
`__init__()` method is used as a constructor method which prototypes an instance
of the class. When we create an object of the class, the `__init__()` method is
called first. The `__init__()` method also requires `self` as the first
parameter.

To initialize the class, we write the name of the class along with parameters
that is accepted by an initializer class. The example below uses a class
`Person` with the initializer method that accepts `first_name`, and `last_name`.
The `self` parameter is itself passed by the class whenever it is called. The
instance `perspn_1` is a variable that has all the features that are prototyped
by the class `Person`.

```python
class Person:
    first_name = ''
    last_name = ''

    def __init__(self, first_name, last_name):
        print("Hi I am Initialized")
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return(f'{self.first_name} {self.last_name}')


person_1 = Person('John', 'Doe')
# prints out "Hi I am Initialized"
```

Here, the statement, `self.first_name = first_name` will set the first name
for an instance `person_1`.

We use `.` notation to access attributes and methods of the instance.

for example, to access the first name, we can write `person_1.first_name`.

```python
person = Person('John', 'Lennon')

# Accessing the attribute
print(person.first_name)    # John

# Accessing the method
print(person.full_name())   # John Lennon
```

### Class Attributes and Instance attributes

### Built-in Class Attributes

### Object

## In python, everything are objects
