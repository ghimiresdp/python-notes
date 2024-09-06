# Chapter 7.4 Encapsulation

**Table of contents**:

- [Chapter 7.4 Encapsulation](#chapter-74-encapsulation)
  - [Introduction](#introduction)
  - [Getter and Setter Methods](#getter-and-setter-methods)
    - [Why do we use Getters and Setters instead of public attributes?](#why-do-we-use-getters-and-setters-instead-of-public-attributes)
  - [The `@property` decorator](#the-property-decorator)
    - [Decorators that are used to create a property in python](#decorators-that-are-used-to-create-a-property-in-python)

## Introduction

Encapsulation is the process of restricting the direct access to the data.
It can be achieved by binding the private attribute along with methods to make
the data usable. In python we make the data protected by naming the attributes
and methods starting with single underscore`_` or double underscores `__`.

The methods that are bound with protected attributes are called as getters and
setters. the **getter** method takes no arguments and **setter** takes one
argument except `self`.

## Getter and Setter Methods

Getter and setter methods are methods that are used to get and set the value of
the private and protected attribute. The example of a getter and setter is as
follows.

```python
class Person:
  def __init__(self):
    self._nickname = 'Unknown'  # Protected Attribute
    self.__age = 0  # Private attribute

  def get_age(self):  # Getter Method
    return self.__age

  def set_age(self, age):  # Setter Method
    self.__age = age


john = Person()
john.set_age(20)
john.get_age()  # 20
```

### Why do we use Getters and Setters instead of public attributes?

> **Teacher**: We Should use setter and getter to access and update private
> attributes

> **Student**: I am now confused !!
>
> - Getter and setter method will help access and update private attributes.
> - Doesn't it mean those attributes are now public?
> - If yes, why don't we use public attributes instead?

**Explanation**:

- It helps hiding or prevents modifying the state of the structured data
  preventing the unauthorized access randomly.
- Suppose changing the state of an attribute should affect another attribute
  the user modifying the public attribute might forget to reflect changes in
  the another.
- Adding the Getter and Setter methods will also help validating the data before
  (and some times after) it gets accessed and updated.

**Example:**

```python
class Person:
  # protected attribute (accessible from outside of class)
  def __init__(self):
    self._age = 0
    self.is_adult = False  # should be true whenever age >=18

  def get_age(self):
    return self._age

  def set_age(self, age):
    self._age = age
    self.is_adult = self._age >= 18


john = Person()
john._age = 20
print(john.is_adult)  # False (not updated)

john.set_age(20)
print(john.is_adult)  # True (updated)
```

Here, when we set age using `john._age = 20`, the value of `is_adult` is not
changed. but as we know, the attribute `is_adult` is dependent on the age value,
the setter method `set_age()` properly handles setting the age as well as the
`is_adult` property too.

## The `@property` decorator

- They look like regular object variables but are capable of attaching custom behavior to the class.
- They are used as better alternative of getters and setters
- Whenever we create a property inside a class, it's behavior will be tightly
  controlled.
- Python properties work similar to methods and behaves similar to variables.

**Why do we use `@property` instead of getters and setters?**

- Property decorators make the function behave like an attribute so that we can
  just use an assignment operator instead of calling a method to access or set
  values of the variable.
- It makes the code look much cleaner than using getters and setters.

### Decorators that are used to create a property in python

- `@property`: used for creating a getter
- `@<property_name>.setter`: Used for creating a setter
- `@<property_name>.deleter`: Used for creating a deleter

**Example:**

```python
class Students:

  def __init__(self, count: int):
    self.__count = count

  @property
  def count(self):  # Getter
    return self.__count

  @count.setter  # Setter
  def count(self, value):
    print("I can do other things while updating my value")
    self.__count = value

  @count.deleter
  def count(self):
    self.__count = 0


class_1 = Students(10)

# without property, we have to call the count() method
# but with property, we can use it like a variable or an attribute
print(class_1.count)

# without property, we have to call the set_count(11) method to change the
# value
# but with property, we can use assignment operator
class_1.count = 11
print(class_1.count)

# instead of deleting the attribute, we added custom behavior that sets count
# to 0 when we use `del` keyword.
del class_1.count
print(class_1.count)
```
