# Python Level 1 Course

> A repository for Python Level 1 course, content, and lab exercises.

This course is specifically designed for my students who are learning basic level python course.

You can always `clone` or `fork` the repository and review the course contents, examples, and attend exercises.

## Contents

1. **Fundamentals of Python**
    - Introduction to Python
    - Python Environment Setup, IDE Setup
    - Hello World in Python
    - Running Python Programs

2. **Data Types and variables**
    - Variables
    - Numbers (boolean, int, long, float, complex)
    - Strings, String Formatting methods
    - Lists
    - Tuples
    - Sets
    - Dictionary
    - Type Hinting in Python (only for python 3.6 and later)
    - Type conversion

3. **Basic Operations**
    - Arithmetic Operations
    - Assignment Operations (single, multiple)
    - Relational Operations
    - Logical Operations
    - Bitwise Operations
    - Membership Operations
    - Identity Operations Advanced Mathematical functions and constants

4. **Decision Making**
    - if statement
    - if else statement
    - if elif else statement

5. **Loops**
    - For Loop
    - While Loop
    - Nested Loop
    - `break`, `continue`, and `pass` statements

6. **Functions**
    - Defining a function
    - Calling a function
    - the `return` statement
    - the `pass` statement
    - Local Variables and Global variables
    - required vs default arguments
    - arguments and keyword arguments
    - function with variable length arguments
    - Anonymous or Lambda functions

7. **Classes**
    - Introduction to **Object Oriented Programming**
    - Class
    - Class Variable and instance variable
    - Methods | Functions vs Methods
    - the `__init__()` method and the `self` parameter
    - built-in class attributes
    - Encapsulation in python [ `_` , `__` in identifier]
    - Object
    - Overrides
    - Operator Overloading

8. **Inheritance**
    - Parent Class
    - Child Class
    - `super()` function
    - Mixins

9. **Python Modules and packages**
    - Introduction to modular programming
    - `__init__.py` file
    - An example of modular python program | importing the module
    - from keyword

10. **File I/O**
    - `open()` function
    - `close()` method
    - `write()` method
    - `read()` method
    - `with` keyword

11. **Exceptions and Exception Handling**
    - Introduction to Exceptions in Python
    - Standard Errors
    - `try`, `except` keyword
    - `try` `except` `else`
    - `finally` keyword
    - `raise` keyword
    - User Defined Exceptions
    - Total

The course has the folder structure as follows:

```
|-- exercises
|    |-- 01_basics.py
|    |-- 02_variables.py
|
|-- res
|    |-- 01_basics.pdf
|    |-- 02_variables.pdf
|  ...
|
|-- 01_basics
|    |-- 01_hello_world.py
|
|-- 02_data_types
|    |-- 01_variables.py
|    |-- 02_numbers.py
|  ...

```

> If you're directly **cloning** the repository, I suggest you to solve in the different branch than the `main` branch to avoid conflicts if the course content changes.



> If you're **forking**, I suggest you not to make any changes in the `main` branch in your repository too so that you can pull and rebase future changes to your `fork`.

## Pulling future changes for your forks

for pulling the future changes you can add `remote` in your local repository with the commands below:

1. Add remote to your local repository
    ```
    git remote add upstream https://github.com/ghimiresdp/python-level1.git

    ```

1. Fetch the changes to your local repository

    ```
    git fetch upstream
    ```

1. checkout to the main branch

    ```
    git checkout main
    ```


1. After fetching, simply merge or rebase your code with either of the commands below:

    - ```
      git rebase upstream/main
      ```
      or
    - ```
      git merge upstream/main
      ```


1. Push to your remote repository

    ```
    git push origin main
    ```

Please do visit my website [sudipghimire.com.np](https://sudipghimire.com.np) to know about my engagements.
