# Exception Handling in python

Exceptions are generally not handled by default and needs handling by writing the code within `try` ... `except` blocks.

## Steps of handling the exception

1. First, try executing the statement(s) inside the `try` block.
2. If the error exists write the program to handle exception in the `except` block.
3. Optionally, we can do certain tasks even if error does not occur.

We can use `try`, `except`, `finally` and `else` statements for handling different kinds of exceptions.

- `try` block is used to try executing our statements
- `except` block handles error during execution. We can have multiple `except` blocks for a `try` statement.
- `else` block executes whenever error does not occur
- `finally` block executes under all circumstances. This block is also known as clean-up block.

The following example shows how to handle the `ZeroDivisionError` using `try` ... `except` blocks:

```python
a = 10
b = 0
try:
    print(a/b)
except:
    print("Hey!! Here comes an error")
```

## Handling multiple exceptions

We can use multiple `except` blocks by specifying different exceptions.

The following function shows how to handle multiple exceptions:

```python
def divide(a, b):
    try:
        print(f"I'm trying to solve the problem: {a} / {b}")
        x = a / b
        print("Hey I solved it")
        return x

    except ZeroDivisionError:
        print("Hey Here comes an error : Zero Division Error")

    except TypeError as e:
        print(f"Error Spotted..{e}")

    except Exception as e:
        print(f"An Unknown Error occured. The error is: {e}")

divide('abc', 'x')    # TypeError is handled
divide(1, 0)        # ZeroDivisionError is handled
```

## Handling errors with `try`, `except`, `else`, and `finally` blocks

```python

list1 = [6, 8, 9, 'John', 'Doe']

def print_index(index: int):
    value = None
    try:
        value = list1[index]
    except IndexError:
        print('There is an error, the index is out of range, the last value would be printed')
        value = list1[-1]
    else:   # this executes only when no error occurs
        print("I did not find any error")

    finally:        # This always execute at the end
        print(f"I Handled the exception when occured. The value is: {value}")


print_index(3)  # runs the `try` block then `else` block and then `finally` block at the end.
print_index(8)  # runs the `try` block, then `IndexError` block and then `finally` block at the end.
```

## Catching Multiple exceptions in the single `except` block

We can catch multiple exceptions by calling them as the tuple of exceptions.

```python
try:
    x = a / b
except (TypeError, ZeroDivisionError) as e:
    print(f"Error Spotted..{e}")
```

The above `except` code block catches both `TypeError` and `ZeroDivisionError` without needing to create different catch blocks.
