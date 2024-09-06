# Errors and Exceptions

Errors that occurs during execution of code are known as exceptions. Some of common exceptions we encounter everyday are as follows:

1. `SyntaxError`
2. `ZeroDivisionError`
3. `IndexError`
4. `KeyError`
5. `ValueError`
6. `NameError`
7. `TypeError`

To know more about exceptions, we can see python documentation for [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

## `SyntaxError`

**Syntax Error** occurs when user enters invalid syntax in the code.
Some of the example codes that give syntax errors are as follows:

```python
x = 5 +     # Syntax Error occurs since + operator used without other value

y = 5 *** 5 # Syntax Error occurs since there is no operation *** in python

SyntaxError: invalid syntax
```

`SyntaxError` is also known as parsing error since if finds unexpected character or a set of characters while parsing the source code.

## `ZeroDivisionError`

Zero division error occurs when we try to divide a number by zero.
if we try to run the following code it gives us `ZeroDivisionError`

```python
x = 5/0
```

The console should print out the following:

```bash
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

## `IndexError`

Index Errors such as  `Index Out Of Range` errors occur when we want to access an item from the collection data using indexes.

```python
x = [1,2,3,4,5]
print(x[10])
```

While executing above line, it gives us `IndexError`.

```bash
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

## `TypeError`

`TypeError` occurs when we try to do operations between unsupported data types.

```python
def add(a,b):
    return a+b
print(add(5, "abc"))
```

While executing above line, it gives us `TypeError`.

```bash
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in add
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

There are numerous built-in exceptions in python. We can check them out in python documentation page.

<https://docs.python.org/3/library/exceptions.html>

## Exception Hierarchy

All Exceptions inherit from the `BaseException` class. The [Class Hierarchy](https://docs.python.org/3/library/exceptions.html#exception-hierarchy) for built-in exceptions is as follows:

```text
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- EncodingWarning
           +-- ResourceWarning
```
