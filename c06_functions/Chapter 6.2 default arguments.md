# Chapter 6.2: Default parameters in functions

**Table of Contents**:

- [Chapter 6.2: Default parameters in functions](#chapter-62-default-parameters-in-functions)
  - [Introduction](#introduction)

## Introduction

While defining function, we can add default values to some or all parameters so
that it takes default value when we do not pass values while calling the
function. We need to add default parameters only after required parameters are
added otherwise it raises an exception

**Example 1:** A program that can add either 2 or 3 numbers

```python
def add_numbers(a, b, c = 0):
    return a + b + c

print(add_numbers(1, 2))        # 3
print(add_numbers(1, 2, 3))     # 6
```

Here, in this example, if we pass 2 arguments `(1,2)`, the default value of `c`
is already `0` so when we call function, it does not give us exception.

If we try to define required parameters after default parameters, then it raises
an exception.

```python
def add_numbers(a=0, b, c):
    return a + b + c
# SyntaxError: non-default argument follows default argument
```

**Example 2:** internationalization

```python
def greet(key, lang='en'):
    words = {
            'hello': {
                'en': 'Hello',
                'fr': 'Bonjour',
                'np': 'नमस्कार',
                'jp': 'こにちは'
            },
            'bye': {
                'en': 'Bye',
                'fr': 'au revoir',
                'np': 'फेरी भेटौला',
                'jp': 'さよなら'
            }
        }
    print(words[key][lang])
greet('hello')          # Hello (default value of lang is 'en')
greet('hello', 'fr')    # Bonjour
greet('hello', 'np')    # नमस्कार
```
