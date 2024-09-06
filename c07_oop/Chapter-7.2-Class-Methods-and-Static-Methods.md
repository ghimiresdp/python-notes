# Chapter 7.2: Class Methods and Static Methods

**Table of contents**:

- [Chapter 7.2: Class Methods and Static Methods](#chapter-72-class-methods-and-static-methods)
  - [Bound and Unbound methods](#bound-and-unbound-methods)
  - [Class Methods](#class-methods)
  - [Static Methods](#static-methods)

## Bound and Unbound methods

**Bound methods** refer to the methods that are bound to either class or an
instance of a class. These method bind values with the class or instance.

In python We have 2 types of bound method:

- Instance-bound methods (regular methods)
- Class-bound methods (class methods)

**Unbound methods** are those methods which lies within the class but are not
bound with any of the attributes of a class. They are also called as
_static methods_.

## Class Methods

Class methods are special kind of methods that are bound to the class instead
of the instance. If we create an instance and try to change any attribute of
the instance, it is not going to accept the changed attribute unless the class
attribute itself is changed.

Class Method is created using the `@classmethod` decorator before a function
definition. A classmethod takes class (generally `cls`) as a first argument.

**Example**: If we have a class called `Animal`, then all animals have 4 legs so
creating any instance should not affect the number of legs of an animal so in
this case, we can create a class method that returns the number of legs of that
class.

```python
class Animal:
  legs = 4

  @classmethod
  def print_legs(cls):
    """
    This method is bound to the class so that class itself is passed instead
    of the instance.
    """
    print('Total no. of legs: ', cls.legs)


cow = Animal()
cow.print_legs()  # 4
cow.legs = 2  # here, instance attribute `legs` value is changed from 4 to 2
cow.print_legs()  # 4
# it will still print 4 since the method is bound to class, but not instance.
```

Classmethods are also useful when you want to work in a **factory pattern**. For
example you have default unit of measurement (suppose radian for angle), you
can create a classmethod to construct an object that will eventually initialize
the angle from degree-equivalent value.

```python
class Angle:
  __PI = 3.14159  # class

  def __init__(self, value):
    self.value = value

  @classmethod
  def from_radians(cls, value):
    return cls(value)

  @classmethod
  def from_degrees(cls, value):
    # this will convert degrees to radians while initializing the a2 instance.
    radians = value * cls.__PI / 180
    return cls.from_radians(radians)


a1 = Angle.from_radians(3.14159)
a2 = Angle.from_degrees(180)

print(a1.value)  # 3.14159
print(a2.value)  # 3.14159

```

## Static Methods

Static Methods are unbound methods that do not bind to either of class or
instance. They just behave like regular functions and are logically grouped
inside of a class just to make code organized and easily accessible. We create
static methods only when we do not require access to any instance-specific data.

Static Method is created using a `@staticmethod` decorator before a function
definition. A static method do not take any of `cls` ir `self` as a first
parameter. We can directly call a staticmethod even without initializing the
class.

Example: if we have length conversion functon that can accept any length, then
the function do not need to take any attributes from the class or the instance.
In this case we can define a static method.

```python
class Length:

  @staticmethod
  def cm_to_m(value):
    """
    A static method is not bound to any class or instance so we do not need
    `self` or `cls` as a first parameter.
    """
    return value / 100

  @staticmethod
  def m_to_cm(value):
    return value * 100


# We can directly call a staticmethod without initializing the class
print(Length.cm_to_m(100))  # 1.0

# we can also call a staticmethod from an instance of the class
l = Length()
l.m_to_cm(2)  # 200
```
