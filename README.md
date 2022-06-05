# Python Notes

**_A repository for Python course notes, examples, and lab exercises targeted to my students and interns._**

This course is specifically designed for my students who are learning basic level python course.

You can `clone` or `fork` the repository and review the course contents, examples, and attend exercises.

## Course Difficulty Level:

- **Chapter 1 - 10**: Easy
- **Chapter 11 - 20**: Medium

## Course Contents _(Links will be updated accordingly)_

1. **[Fundamentals of Python](course/c01_basics/)**
   - [Introduction to Python](course/c01_basics/Chapter%201%20Basics.md)
   - [Python Environment Setup, IDE Setup](course/c01_basics/Chapter%201%20Basics.md#installing-python)
   - [Hello World in Python](course/c01_basics/Chapter%201%20Basics.md#hello-world-with-idle)
   - [Running Python Programs](course/c01_basics/Chapter%201%20Basics.md#creating-editing-and-running-python-files)
   - comments and documentation
       - Single Line Comments
       - inline Comments
       - Multiline Comments
       - Docstrings
   - indentation
   - [Chapter 1 Quiz](course/c01_basics/quiz/README.md)

2. **[Data Types and variables](course/c02_data_types/)**
    - [Variables](course/c02_data_types/Chapter%202.1%20Variables.md)
    - [Numeric Data Types](course/c02_data_types/Chapter%202.2%20Numeric%20Data%20Types.md)
    - [Strings](course/c02_data_types/Chapter%202.3%20Strings.md)
    - [String Formatting](course/c02_data_types/chapter%202.4%20string%20formatting.md)
    - Lists
    - Tuples
    - Sets
    - Dictionary
    - Type Hinting in Python (only for python 3.6 and later)
    - Type conversion

3. **[Basic Operations](course/c03_operations/)**
    - Arithmetic Operations
    - Assignment Operations (single, multiple)
    - Relational Operations
    - Logical Operations
    - Bitwise Operations
    - Membership Operations
    - Identity Operations
    - Advanced Mathematical functions and constants

4. **[Decision Making](course/c04_decision_making/)**
    - if statement
    - if else statement
    - if elif else statement

5. **[Loops](course/c05_loops/)**
    - For Loop
    - While Loop
    - Nested Loop
    - `break`, `continue`, and `pass` statements

6. **[Functions](course/c06_functions/)**
    - Defining a function
    - Calling a function
    - the `return` statement
    - the `pass` statement
    - Local Variables and Global variables
    - required vs default arguments
    - arguments and keyword arguments
    - function with variable length arguments
    - Anonymous or Lambda functions

7. **[Classes](course/c07_oop/)**
    - Introduction to **Object Oriented Programming**
    - Class
    - Class Variable and instance variable
    - Methods,  Functions vs Methods
    - the `__init__()` method and the `self` parameter
    - built-in class attributes
    - Object
    - Encapsulation in python [ `_` , `__` in identifier]
    - getters and setters
    - Overrides
    - Operator Overloading
    - class methods and static methods
    - inheritance
      - Parent Class
      - Child Class
      - `super()` function
      - Mixins

8. **[Python Modules and packages](course/c08_modules_packages/)**
    - Introduction to modular programming
    - `__init__.py` file
    - An example of modular python program | importing the module
    - from keyword
    - `datetime` module
    - `random` module
    - `json` module

9. **[File I/O](course/c09_file/)**
   - `open()` function
   - `close()` method
   - `write()` method
   - `read()` method
   - `with` keyword

10. **[Exceptions and Exception Handling](course/c10_exceptions/)**
    - Introduction to Exceptions in Python
    - Standard Errors
    - `try`, `except` keyword
    - `try` `except` `else`
    - `finally` keyword
    - `raise` keyword
    - User Defined Exceptions
    - Total

11. **[Python Package Management](course/c11_pip/)**
	- [Introduction to Symantic Versioning](course/c11_pip/c1101%20symver.md)
	- [PIP and its usage](course/c11_pip/c1102%20pip.md)

12. **[Virtual Environments](course/c12_virtual_environment/)**
	- [Introduction to virtual enviromnemts](course/c12_virtual_environment/c1201%20virtual%20environment%20intro.md)
	- [VENV and its usage](course/c12_virtual_environment/c1202%20venv.md)
	- [PIPENV and its usage](course/c12_virtual_environment/c1203%20pipenv.md)

13. **[Python Advanced Functions](course/c13_advanced_functions/)**
    - [`groupby()` function](course/c13_advanced_functions/chapter%2013.1%20groupby.md)
    - [`sorted()` function](course/c13_advanced_functions/chapter%2013.2%20sorted.md)
    - [`filter()` function](course/c13_advanced_functions/chapter%2013.3%20filter.md)
    - [`map()` function]()

14. **[Regular Expressions (REGEX)](course/c14_regex/)**
    - [Introduction to regular expressions](course/c14_regex/chapter%2014.1%20regular%20expressions.md)
    - [REGEX special characters](course/c14_regex/chapter%2014.2%20regex%20special%20characters.md)
    - [The `re` module](course/c14_regex/chapter%2014.3%20the%20re%20module)

15. [**Advanced Data Structures**](course/c15_data_structures/)
16. [**Decorators**](course/c16_decorators/)
17. [**Mixins**](course/c17_mixins/)
18. [**`http` module**](course/c18_python_http/)
19. [**`requests` library**](course/c19_requests/)
20. [**Advanced Type hinting**](course/c20_advanced_type_hinting/)

## Folder Structure
The repository has its folder structure as shown in example below:
```
📂 python-level1
 |-- 📂 course
 |    |-- 📂 chapter_1
 |    |    |-- 📜 chapter 1 theory 1.md
 |    |    |-- 📜 chapter 1 theory 2.md
 |    |    |-- 📄 ...
 |    |    |-- 📂 code
 |    |    |    |-- 📄 c0101.py
 |    |    |    |-- 📄 c0102.py
 |    |    |    |-- 📄 ...
 |    |    |
 |    |    |-- 📂 quiz
 |    |    |    |-- 📜 chapter 1 quiz.md
 |    |    |    |-- 📂 solutions
 |    |    |         |-- 📄 solution_1.py
 |    |    |         |-- 📄 solution_2.py
 |    |    |         |-- 📄 ...
 |    |
 |    |-- 📂 ...
 |
 |-- 📂 projects
 |    |-- 📂 project_1
 |    |    |-- 📜 Project 1 Requirement Specification.md
 |    |    |-- 🗃️ Media file for Requirements
 |    |    |-- 🗃️ ...
 |    |    |-- 📂 project_1 (solution)
 |    |         |-- 📂 contents
 |    |         |-- 📄 contents
 |    |         |-- 📄 contents
 |    |
 |    |-- 📂 ...

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
