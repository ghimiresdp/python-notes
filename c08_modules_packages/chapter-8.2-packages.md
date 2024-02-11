# Chapter 8.2 Python Packages

- A python package is a directory that contains multiple python files or modules
- A package contains a special file `__init__.py` as the initializer file.
- it might contain subdirectories or subpackages too.

## Basic Package directory structure

```
📁 my_package/
  |-- 📄 module_1.py
  |-- 📄 module_2.py
  |-- 📄 module_3.py
  |-- 📄 __init__.py
```

## Basic Package structure with subpackage inside it

```
📁 my_package/
  |-- 📁 pkg_1/
  |     |-- 📄 __init__.py
  |     |-- 📄 pkg1_module_1.py
  |     |-- 📄 pkg1_module_2.py
  |
  |-- 📄 __init__.py
  |-- 📄 module_1.py
  |-- 📄 module_2.py
  |-- 📄 module_3.py
```

## The `__init__.py` file

The `__init__.py` file is the initializer for the package that is capable of importing all the components inside of the modules of the package.

It is capable of creating shortcuts so that user do not need to go deeper to import required components. To create a shortcut, we can simply import everything from the modules from the package.

Eg: ** `__init__.py`  of package: `my_package`

```python
from .module_1 import Class1, Class2
from .pkg_1.pkg1_module_1 import *
```

after importing all elements with the above command, we can replace the following command

```python
from my_package.module_1 import Class1
from my_package.pkg_1.module_1 import ABC

```

with the following command:

```python
from my_package import Class1, ABC
```
