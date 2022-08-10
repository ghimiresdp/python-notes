- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

[go to course contents](https://github.com/ghimiresdp/python-level1/)
<hr>

# Chapter 6.1: Function

- [Chapter 6.1: Function](#chapter-61-function)
    - [Introduction](#introduction)
    - [The `return` statement](#the-return-statement)
    - [Function with arguments](#function-with-arguments)

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

**Example 1:** a function that accepts 2 arguments and returns the added number.

```python
def add_me(num_1, num_2):
    return num_1 + num_2

result_1 = add_me(4, 5)
print(result_1) # 9

result_2 = add_me(10, 5)
print(result_2) # 15

```

**Example 2:** A function that finds out the simple interest

```python

def simple_interest(principal, time, rate):
    return (principal * time * rate) / 100

si_1 = simple_interest(1000, 2, 10) # 200
si_2 = simple_interest(5000, 3, 20) # 3000
```
