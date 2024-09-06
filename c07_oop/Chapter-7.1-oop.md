# Chapter 7.1 Object-Oriented Programming (OOP)

**Table of contents**:

- [Chapter 7.1 Object-Oriented Programming (OOP)](#chapter-71-object-oriented-programming-oop)
  - [Introduction to OOP](#introduction-to-oop)
    - [Building blocks of an OOP](#building-blocks-of-an-oop)
    - [Features Of Object-Oriented Programming](#features-of-object-oriented-programming)
  - [Python Classes](#python-classes)
    - [PEP-8 Conventions for prototyping a class](#pep-8-conventions-for-prototyping-a-class)
    - [What is `self`?](#what-is-self)
  - [Basic Building block of Classes](#basic-building-block-of-classes)
    - [Attributes, Methods, and the `self` parameter](#attributes-methods-and-the-self-parameter)
    - [Initializing the class, Constructor Method, and uses of `self`.](#initializing-the-class-constructor-method-and-uses-of-self)
    - [Class Attributes and Instance attributes](#class-attributes-and-instance-attributes)
    - [Built-in Class/Instance Attributes](#built-in-classinstance-attributes)
    - [Object or Instance](#object-or-instance)

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
are integers, but there is no sense adding those values. There is no binding
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

A class is a building block of an OOP. A class creates a block of a code that is
used to bind attributes to its methods. Class works just like a group or a
container that contains different variables and functions.

Python classes can be created using a `class` keyword.

### PEP-8 Conventions for prototyping a class

- Class names should be written in `UpperCamelCase`.
- Class attributes and methods should be written in `snake_case`.
- We should separate classes with 2 blank lines and methods with a blank line.
- objects or instances are defined with `snake_case` representation as in
  variables.

**A Basic Example:**

```python
class Person:
  first_name = 'John'
  last_name = 'Doe'

  def show_full_name(self):
    return f'{self.first_name} {self.last_name}'
```

The above example uses `first_name` and `last_name` as attributes of the class
`Person` whereas `show_full_name()` as the method that binds to the person

### What is `self`?

`self` is just an identifier or a variable name that holds the instance of
the class. `self` is not a python keyword and can be replaced with any other
identifier, but to make code consistent, pep-8 prefers using `self` as the
first parameter.

## Basic Building block of Classes

Classes are made up of the following building blocks:

- **Attributes**
  - Class Attributes
  - Instance Attributes
- **Methods**
  - Instance Methods (Bounded to the instance)
  - Class Methods (Bounded to the class)
  - Static Methods (Unbounded methods)
  - Initializer method (called upon creation of the instance)
- **Instance**

### Attributes, Methods, and the `self` parameter

- All the **variables** defined inside a class are **attributes**.
- Attribute acts as a state of the class which changes over time and condition
- All functions defined inside a class are known as methods
- All instance methods use `self` as the first parameter which references the
  instance itself.
- the `__init__()` method do not need to be called and gets automatically called
  once the object gets initialized.

```python
class Person:
  species = 'Human'  # Class Attribute

  def __init__(self, first_name, last_name):  # initializer method
    self.first_name = first_name    # Instance Attribute
    self.last_name = last_name

  def fullname(self):  # method
    print(f"{self.first_name} {self.last_name}")

```

### Initializing the class, Constructor Method, and uses of `self`

The constructor method is a method that initializes the class. in python,
`__init__()` method is used as a constructor method which prototypes an instance
of the class. When we create an object of the class, the `__init__()` method is
called first. The `__init__()` method also requires `self` as the first
parameter.

To initialize a class, we write the name of the class along with parameters
that is accepted by an initializer class. The example below uses a class
`Person` with the initializer method that accepts `first_name`, and `last_name`.
The `self` parameter is itself passed by the class whenever it is called. The
instance `perspn_1` is a variable that has all the features that are prototyped
by the class `Person`.

```python
class Person:
  species = 'Human'  # Attribute

  def __init__(self, first_name, last_name):  # initializer method
    """
    This initializer method is called automatically when we create an instance
    of the class. The parameters that is required in the `__init__()` method
    should be passed while instantiating an object of the class.
    """
    print("Hi I am Initialized")
    self.first_name = first_name
    self.last_name = last_name

  def fullname(self):  # method
    print(f'{self.first_name} {self.last_name}')

# The `Person` takes 2 arguments while initializing since the `__init__()`
# method requires 2 arguments `first_name` and `last_name`.
person_1 = Person('John', 'Doe')
# prints out "Hi I am Initialized"
```

Here, the statement, `self.first_name = first_name` will set the first name
for an instance `person_1` once `person_1 = Person('John', 'Doe')` gets
executed.

We use `.` notation to access attributes and methods of the instance.

for example, to access `first_name`, we can write `person_1.first_name`.

```python
person = Person('John', 'Lennon')

# Accessing the attribute
print(person.first_name)  # John

# Accessing the method
print(person.full_name())  # John Lennon
```

> **Note**: _Even though methods has `self` as the first parameter, we do not
> need to pass the `self` argument manually to call the function. It
> automatically gets passed by the python interpreter in the time of calling._
>
> Also, the `self` parameter is only accessed inside the class body and has
> special privilege to access all the private and protected attributes of the
> class.

### Class Attributes and Instance attributes

Those Attributes that are declared during the class definition are known as
_class attributes_. The class attribute points out the class
and is accessible even before initialization of the class.

On the other hand, Instance attributes are declared inside the `__init__()`
method and are only accessible after initializing the class.
If we want to declare an instance attribute, we need to define an attribute
using `self` annotation otherwise it would create a local variable instead of an
instance attribute.
The example below shows different attributes declared within a class.

```python
class Animal:
  category = 'Vertebrate'  # Class Attribute
  legs = 4

  def __init__(self, name, child):
    self.name = name  # Instance Attribute
    self.child = child
    word = 'Moo'  # Local variable (Inaccessible outside of a method)


print(Animal.category)  # Vertebrate
cow = Animal(name='My Cow', child='calf')
print(cow.name)  # My Cow
```

- To access the class attribute `category`, we do not need to instantiate the
  class.
- To access the instance attribute `name`, we need to instantiate the class by
  using `Animal(name='My Cow', child='calf')`
- If we try to access the instance attribute `name` without initializing the
- class, it raises an `AttributeError` exception.

  `type object 'Animal' has no attribute 'name'` as below.

```pycon
>>> print(Animal.name)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    Animal.name
AttributeError: type object 'Animal' has no attribute 'name'
```

### Built-in Class/Instance Attributes

Python classes has some built-in attributes which will be available to all
classes. some of the attributes are as follows:

- `object.__str__()`: returns the readable string representation of the object
- `object.__repr__()`: returns the unambiguous string representation similar to
  the `__str__()` method.
- `object.__dict__`: the dictionary representation of the object
- `object.__doc__`: the documentation string of the class
- `object.__sizeof__()`: returns the size of object in bytes

**Example:**

```python
class Person:
  """
  The class Person stores the first_name, last_name, and age of a
  person once initialized.
  """

  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

  def __str__(self):
    return f'Person<{self.first_name}>'


john = Person('John', 'Lennon', 50)

print('The String Representation is:', john.__str__())
print('The dictionary representation is:', john.__dict__)
print('The document string is:', john.__doc__)
print('The size of a class is:', john.__sizeof__())
```

**Output:**

```
The String Representation is: Person<John>
The dictionary representation is: {'first_name': 'John', 'last_name': 'Lennon', 'age': 50}
The document string is:
    The class Person stores the first_name, last_name, and age of a
    person once initialized.

The size of a class is: 32
```

### Object or Instance

In python, everything are objects. Even basic data types such as `int`, `float`,
etc. are also represented using classes.

**Example**:

```py
x = 5
print(type(x))

# <class 'int'>
```

Here `x` is an object of a class `int`. Hence it inherits all the properties and
features defined in the class `int`.

In python once we initialize a class and assign the instance to the variable,
the variable is called as an object or instance. for example:

```python
class Animal:
  def __init__(self, name, word):
    self.name = name
    self.word = word

    def speak(self):
      print(f'I speak with {self.word}')


cow = Animal('My Cow', 'Moo')
```

Here `cow` is an instance of `Animal()` hence `cow` inherits all properties of
the class `Animal` such as `speak()`.
