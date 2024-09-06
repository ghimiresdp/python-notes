# Chapter 7.5: Inheritance and Polymorphism

**Table of contents**:

- [Chapter 7.5: Inheritance and Polymorphism](#chapter-75-inheritance-and-polymorphism)
  - [Inheritance](#inheritance)
    - [The `super()` function](#the-super-function)
    - [Single Inheritance](#single-inheritance)
    - [Multiple Inheritance](#multiple-inheritance)
    - [Hierarchical Inheritance](#hierarchical-inheritance)
    - [Multilevel Inheritance](#multilevel-inheritance)
    - [Hybrid Inheritance](#hybrid-inheritance)
    - [Builtin Functions to check the relationship between different classes](#builtin-functions-to-check-the-relationship-between-different-classes)
      - [the `isinstance()` function](#the-isinstance-function)
      - [the `issubclass()` function](#the-issubclass-function)
- [Polymorphism](#polymorphism)

## Inheritance

Inheritance is the process of transferring the attributes and behaviors of the
parent class to the child class. This concept is similar to the biological
inheritance where child inherits the feature of parent.

The base class from which all the features are inherited is called the parent
class and the class which inherits parent's features is called a child class.

**Basic Structure of an inheritance:**

```python
class Parent:
    < parent_attributes >
    < parent_methods >


class Child(Parent):
    # here all the parent attributes and methods are automatically inherited to
    # the child class.
    < child_attributes >
    < child_methods >
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


r1 = Rectangle(10, 20)
print(r1.area())  # 200

sq1 = Square(10)
print(sq1.area())  # 100
```

In the above example, the class Square do not have any method defined to find
the area, but as it is a child of a class `Rectangle`, it inherits the method
`area()` from the parent class `Rectangle`.

### The `super()` function

In an above example we could see the usage of `super()` function. The `super()`
function returns objects represented in the parent's class and is very useful in
case of inheritance.

The Benefits of using `super()` method in python are as follows:

- We can directly access the attributes of the parent class
- We can isolate the changes of the super class with the child class with the
  help of a `super()` method.

**Example**

```python
class Animal:
    def __init__(self):
        self.legs = 4
        self.tail = True


class Dog(Animal):
    def __init__(self):
        self.is_domestic = True
        super().__init__()


d1 = Dog()
print(d1.legs, d1.tail)  # 4 True
```

Here, the instance of Dog only has the instance attribute `is_domestic`, but if
we check `d1.legs`, then it gives `4` since the initializer method of the class
`Dog` also initializes the parent class `Animal` with the help of `super()` as
shown below.

```python
def __init__(self):
    ...
    super().__init__()
```

**Types of Inheritance**

There are various types of inheritance which are as follows:

1. **Single Inheritance**: Single parent and a single child
2. **Multiple Inheritance**: Multiple parents and a single child
3. **Hierarchical Inheritance**: Single parent and multiple children
4. **Multilevel Inheritance**: Child, Parent, Grandparent, etc.
5. **Hybrid Inheritance**

### Single Inheritance

Single Inheritance refers to the inheritance in which a child class inherits
attributes and features from a parent class.

```python
class Animal:
    has_tails = True


class Cow(Animal):
    # Here, Cow inherits attribute (has_tails) from the parent class Animal.
    pass
```

### Multiple Inheritance

Multiple Inheritance is a type of inheritance in which a class inherits features
from more than 1 parent classes. In multiple inheritance, Python uses C3
Linearization algorithm to determine the order in which to resolve class
attributes and methods. The process is also known as Method Resolution Order
(MRO). To learn more about C3 linearization, you can check the link below:
<https://en.wikipedia.org/wiki/C3_linearization>

```python
class CoffeeShop:
    latte = 2
    Espresso = 1.5

    def prepare_coffee(self):
        pass


class Bakery:
    doughnut = 2
    latte = 2.5

    def make_doughnut(self):
        pass


class Restaurant(CoffeeShop, Bakery):
    Burger = 3

    def prepare_burger(self):
        pass
```

Here, Class Restaurant inherits all attributes and methods from its parent
classes however as `latte` is available in both of the parent classes, it uses
MRO to select the attribute `latte` from `CoffeeShop` since it is the first
parent class.

### Hierarchical Inheritance

Hierarchical inheritance is similar to single inheritance. In Hierarchical
inheritance, one parent class is inherited by multiple children classes. We can
see, each child class can be separately seen as a singly inherited class.

```python
class Vehicle:
    wheels = 4
    engine = 'Diesel'

    def ignite(self):
        pass

    def horn(self):
        pass


class Bus(Vehicle):
    wheels = 6


class Car(Vehicle):
    engine = 'Petrol'
```

Here, A single Parent class `Vehicle` is inherited by multiple child classes
`Bus` and `Car`. In `Bus`, the attribute `wheels` is overwritten but `engine` is
inherited from parent whereas in `Car`, `engine` is overwritten but `wheels` is
inherited. all classes that inherit `Vehicle` also inherits function such as
`horn()` and `ignite()`.

### Multilevel Inheritance

Multilevel inheritance is a type of inheritance in which a child class inherits
its characteristics from a parent class, which also inherit characteristics from
its parent class. We can also call the base class as a grandparent class.

```python
class Vehicle:
    wheels = 4
    transmission = 'manual'

    def ignite(self):
        pass


class TwoWheeler(Vehicle):
    wheels = 2
    engine = 'Petrol'


class Scooter(TwoWheeler):
    transmission = 'Automatic'

```

Here the class `Scooter` inherits attributes and methods from `TwoWheeleer` and
the `TwoWheeler` inherits attributes from `Vehicle`, hence, the class inherits
features from `Vehicle` too. This type of inheritance is known as multilevel
inheritance. Here, `TwoWheeler` is a parent class and `Vehicle` is a grandparent
class of `Scooter` so it inherits `ignite()` method from the grandparent class.

### Hybrid Inheritance

Hybrid Inheritance is a mix of all inheritance where we can see different levels
of classes are inherited.

```python
class Engine:
    def ignite(self):
        pass


class Vehicle(Engine):
    max_seat = 6

    def horn(self):
        pass


class RoadTransport:
    has_wheels = True


class Bus(Vehicle, RoadTransport):
    max_seats = 50


class Helicopter(Vehicle):
    def take_off(self):
        pass

```

Here `Helicopter` inherits `Vehicle` which again inherits `Engine`, which is a
kind of multilevel inheritance but the class `Bus` inherits `Vehicle` as well as
`RoadTransport` where we can see Hybrid inheritance. In this case if we see
class `Vehicle`, we can see multilevel inheritance, but if we consider both of
the parent classes, then it is multiple inheritance. Such mixed inheritance is
also known as hybrid inheritance.

### Builtin Functions to check the relationship between different classes

There are some methods that is used to check an object is an instance of a class
or a parent class.

#### the `isinstance()` function

The `isinstance()` method returns true if the object is an instance of the class
or any parent classes (if exists).

**Example**:

```python
class Vehicle:
    pass


class Car(Vehicle):
    pass


c = Car()
v = Vehicle()
print(isinstance(c, Car))  # True
print(isinstance(c, Vehicle))  # True

print(isinstance(v, Vehicle))  # True
print(isinstance(v, Car))  # False
```

Here, we can see that the object of a child class is an instance of the parent
class, but the object of a parent class is not an instance of the child class.

#### the `issubclass()` function

The `issubclass()` method returns true if the class is a subclass of another
class. This function is useful when we need to check if there is inheritance
between two classes.

```python
class Vehicle:
    pass


class Car(Vehicle):
    pass


print(issubclass(Car, Vehicle))  # True
print(issubclass(Vehicle, Car))  # False (it is a superclass instead)
```

# Polymorphism

The term polymorphism refers to the state of having many forms. In OOP concept,
an abstract class defines the function and the behavior of the function is
different across classes inherited from that class.

**Example**

```python
class Shape:
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius ** 2
```

Here, the method `area()` has different forms in the above example. if it is a
rectangle, the value of `area()` will depend upon the length and width of the
rectangle however, the same `area()` function behave differently in case of the
`Circle` class. This difference in the behavior of the same function in OOP is
known as polymorphism.
