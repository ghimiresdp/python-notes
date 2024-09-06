# Chapter 6.4: Recursive Function

**Table of Contents**:

- [Chapter 6.4: Recursive Function](#chapter-64-recursive-function)
  - [Introduction](#introduction)

## Introduction

Recursive function is a function which calls itself. A recursive function is
generally created to iterate over the dynamic parameter until it reaches the
recursion limit. Recursive function contains 2 different elements:

1. recursion limit
2. recursive function call

**Basic Syntax**

```python
def function_name(params):
    if condition:
        function_name(updated_params)
    else:   # recursion Limit
        return final_value
```

**Example 1:** A recursive function that prints out the factorial of a number.

- `5 ! = 5 * 4 * 3 * 2 * 1 = 120`
- `0 ! = 1`

```python
def factorial(n):
    if n > 0:
        return(n * factorial(n-1))
    return 1

print(factorial(7))     # 5040
```

**Example 2:** A recursive function that prints out the first nth item of a
fibonacci series `1, 1, 2, 3, 5, 8, 13, 21, 34, ...`.

```python
def fibonacci(n):
    if n > 1:
        return(fibonacci(n-1) + fibonacci(n-2))
    return n

item = fibonacci(7)

print(item)     # 13
```

**Example 3:** A recursive function to convert decimal to binary

```python
def dec2bin(n: int):
    if n != 0:
        return dec2bin(n // 2) * 10 + n % 2
    else:
        return 0

print(dec2bin(14))  # 1110
```
