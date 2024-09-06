# Chapter 8.1 Python Modules

- Module is a collection of different classes, functions and variables
- A module is nothing but a single file which can be imported into another file.

## basic structure of a module

```shell
📁 working_dir/
    |-- 📄 module.py
    |     📦 variables
    |     📦 functions
    |     📦 classes
    |
    |-- 📄 main.py
          📦 imports from module.py
          📦 extra logic/code
```

File 1: `school.py`

```python
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
```

File 2: `main.py`

```python
from school import Student
john = Student('John Doe', 1)
jane = Student('Jane Doe', 1)
```

## Importing the whole module

if `animal.py` is the filename for the module, the name of the module would be `animal`. so we can import the whole module by the following command.

```python
import animal
```

Importing the whole module imports everything that is defined, imported, and initialized inside the module.

## Importing individual elements from the module

we can use `from` keyword to import the individual component from the module. For example the module `animal` contains the class `DomesticAnimal`, we can import it using the following command.

```python
from animal import DomesticAnimal
# we can also import multiple elements in the single line using comma
from animal import DomesticAnimal, WildAnimal

# we can also use small brackets so that we can import in different lines

from animal import (
    Animal,
    DomesticAnimal,
    WildAnimal,
)
```
