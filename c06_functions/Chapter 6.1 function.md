# Chapter 6.1: Function

**Table of Contents**:

- [Chapter 6.1: Function](#chapter-61-function)
  - [Introduction](#introduction)
  - [The `return` statement](#the-return-statement)
  - [Function with arguments](#function-with-arguments)
  - [Local, Non-local and Global variables](#local-non-local-and-global-variables)
    - [The `global` keyword](#the-global-keyword)
    - [The `nonlocal` keyword](#the-nonlocal-keyword)

## Introduction

Function is a block of code that runs when it is called. Unlike other statements
function does not execute unless it is called. There are 2 steps in using a
function in our code, i.e. **Function Definition** and **Function Call**. We
need to define or prototype a function and then we can call it whenever it is
necessary.

Some of the characteristics of function are as follows:

- a block of code that runs when it is called
- provides organized, reusable and modular code
- used for reducing duplicates
- takes zero or more parameters as arguments
- returns either a value or `None`
- returns a tuple when multiple values needs to be returned
- declared using `def` keyword
- it can have any type of arguments eg: `int`, `float`, `list`, `Callable` or
  even `object`
- unlike other programming languages, python function body can not be empty. If
  we want to create an empty function body, we can use `pass` statement.
- similar to branching and loops, function body also needs indented code block.

example of builtin functions:

- `print()`
- `input()`
- `len()`

**Basic structure**

```python
def <function_name> (<arg1>, <arg2>, .., <arg_n>,):
    statement[s]
```

**PEP 8 Guidelines for defining a python function**

- python functions are created using `snake_case` names
- top level functions are separated with 2 blank lines
- parameters inside functions are separated by comma`,` along with spaces
- we should not surround `=` with spaces while using named
  parameters and default vaues.
- python function argument type is hinted with the type using `:`
- function return type is hinted with right arrow (`-` and `>` sign). i.e. `->`

**Example:** Basic Function definition

```python
def my_function():
    print("I am inside the function")

print('I am outside of the function')
my_function()
my_function()
```

In the above code, the function `my_function()` is defined or prototyped using
`def` keyword. the empty parenthesis `()` represents that there are no
arguments that needs to be passed to the function. Whenever it is called, it
should print `'I am inside the function'`.

## The `return` statement

The `return` statement returns the value or the output of the function that is
then feed to other variables for further computation. The value that is returned
can be assigned to other variable or printed directly to the console, or
sometimes passed as an argument to other functions also.

**Example:**

```python
def say_hi():
    return 'Hi there!!'

x = say_hi()    # x will have value of 'Hi there!!'

print(say_hi())
# directly prints 'Hi there!!' since it is returned and passed as an argument to
# another function `print()`
```

## Function with arguments

Programming is made dynamic with the help of functions that accept arguments.
Whenever we call the function, we can pass arguments so that our code can be
made more modular and reusable.

**Note:** <i>If we pass less or more arguments than expected, then it raises the
`TypeError` saying either the argument is missing or more arguments given.</i>

**Example 1:** a function that accepts 2 arguments and returns the added number.

```python
def add_me(num_1, num_2):
    return num_1 + num_2

result_1 = add_me(4, 5)
print(result_1) # 9

result_2 = add_me(10, 5)
print(result_2) # 15

```

**Example 2:** A function that finds out the simple interest along with type
hinting

```python

def simple_interest(principal: float, time: int, rate: float) -> float:
    return (principal * time * rate) / 100

si_1 = simple_interest(1000, 2, 10) # 200
si_2 = simple_interest(5000, 3, 20) # 3000

si_3 = simple_interest(1000, 2)
# TypeError: simple_interest() missing 1 required positional argument: 'rate'


si_3 = simple_interest(1000, 2, 10, 5)
#TypeError: simple_interest() takes 3 positional arguments but 4 were given

```

**Example 3:** A function that has loop inside it

```python
def print_multiple(value, iteration):
    for x in range(1, iteration+1):
        print(f'iteration {x}:', value)

print_multiple('Hello there!!', 5)
```

**Output:**

```
iteration 1: Hello there!!
iteration 2: Hello there!!
iteration 3: Hello there!!
iteration 4: Hello there!!
iteration 5: Hello there!!
```

**Example 4:** A function that returns the double of a number if it is even and
triple of a number if it is odd.

```python

def double_triple(number):
    if number % 2 == 0:
        return 2 * number
    else:
        return 3 * number

print(double_triple(4)) # 8
print(double_triple(5)) # 15

# functions can also be used in comprehensions
list_1 = [double_triple(n) for n in range(1, 6)]
print(list_1)
# [3, 4, 9, 8, 15]
```

## Local, Non-local and Global variables

- **Global Variables** are those variables which are not defined inside
  any function and have a global scope.
- **Local Variables** are those variables which are defined inside a
  function and it's scope is limited to that function only.

**Example 1:** variable scopes

```python
x = 10  # global variable
def my_function():
    y = 20      # local variable (it's scope is only inside a function)
    print(x)    # 10

def my_next_function():
    print(x)    # 10 since there is no local variable x, it uses global one

print(x)        # 10
my_function()
# print(y)      # raises an exception since it is a local variable.
```

**Example 2:**

```python
message = 'Hello world'

def my_function():
    message = 'Hi there'
    print(message)  # Hi there
my_function()
print(message)  # Hello world
```

Here, even the variable `message` was initialized as a global variable,
redefining it inside the function does not impact the global variable. once the
scope of the local variable ends, the value will be default to the global value.

### The `global` keyword

If we want to access the global variable inside the function, it is possible
but whenever we want to assign the value of the global variable and try to
access it, it instead creates a new local variable with scope inside of the
function. To avoid this, we use the `global` keyword.

```python
x = 'Hello world'
def my_function():
    global x
    x = 'Hi there'
my_function()
print(x)    # Hi there
```

### The `nonlocal` keyword

Non-local variables are those variables which are declared within nested
functions. Non-local refers to the local variables of the outer function. We
use `nonlocal` keyword to access those variables of outer functions which are
not global.

```python
x = 10
def outer_function():
    x = 20
    def inner_function():
        nonlocal x
        x += 10
        print('The value of non-local x = ', x)
    print('Before calling inner function, x = ', x)
    inner_function()
    print('After calling inner function, x = ', x)
outer_function()
print('After calling outer function, x = ', x)
```

**Output:**

```
Before calling inner function, x =  20
The value of non-local x =  30
After calling inner function, x =  30
After calling outer function, x =  10
```
