- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

[go to course contents](https://github.com/ghimiresdp/python-level1/)
-----------------------

# Chapter 3.3. Dictionary

**Table of Contents**

- [Chapter 3.3. Dictionary](#chapter-33-dictionary)
    - [Introduction](#introduction)
    - [Creating a dictionary](#creating-a-dictionary)
    - [Adding/updating an item to the dictionary](#addingupdating-an-item-to-the-dictionary)
    - [Adding/updating multiple items to the dictionary](#addingupdating-multiple-items-to-the-dictionary)
    - [removing an item from the dictionary](#removing-an-item-from-the-dictionary)
    - [popping out an arbitrary item from the dictionary](#popping-out-an-arbitrary-item-from-the-dictionary)
    - [getting keys, values and items of the dictionary](#getting-keys-values-and-items-of-the-dictionary)
    - [Some useful dictionary methods](#some-useful-dictionary-methods)

## Introduction

We can visualize python dictionaries as regular dictionary book. If we want to find the meaning of the word `apple`, we
search for the keyword `apple` and find the value associated to it.

Dictionaries in python are similar to lists but contains key-value pairs. We generally access items of the dictionary
using the key instead of index.

Some of the features of dictionary are as follows:

- Dictionaries are similar to lists but represented by _key-value_ pairs
- Dictionaries are ordered (since python 3.7)
- They are written inside _curley-brackets_ or _braces_ `{}`
- Keys must be unique otherwise the later one replaces the original one
- Dictionaries are mutable.
- Dictionaries can have multiple data types in their key-value pair

**Structure/syntax**

```python
{key_1: value_1, key_2: value2, ...}

# multiline
{
    key_1: value_1,
    key_2: value_2,
    ...
        key_n: value_n
}

```

## Creating a dictionary

We can create a dictionary by adding key value pairs within curley brackets.

**Example 1:**

```python
dict_1 = {'a': 1, 'b': 2, 'c': 3}
```

**Example 2:**_multiline dictionary_

```python
person = {
    'name': 'Spock',
    'age': 20,
    'married': False,
    'positions': ['Lieutenant', 'Captain', 'Commander'],
}
```

**Example 3:** _If we add the duplicate key, the second key-value pair replaces the original one_

```python
person = {
    'name': 'Spock',
    'age': 20,
    'married': False,
    'age': 21,
}
print(person)

# Out: {'name': 'Spock', 'age': 21, 'married': False}
```

## Adding/updating an item to the dictionary


## Adding/updating multiple items to the dictionary

## removing an item from the dictionary

## popping out an arbitrary item from the dictionary

## getting keys, values and items of the dictionary

## Some useful dictionary methods

- `dict.copy()`
- `dict.fromkeys()`
- `dict.setdefault()`
- `dict.clear()`
