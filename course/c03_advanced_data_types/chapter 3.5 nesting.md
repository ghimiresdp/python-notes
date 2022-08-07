- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

[go to course contents](https://github.com/ghimiresdp/python-level1/)
-----------------------

# Chapter 3.5. Nesting of Iterables

**Table of Contents**
- [Chapter 3.5. Nesting of Iterables](#chapter-35-nesting-of-iterables)
- [Introduction to nesting](#introduction-to-nesting)
    - [Creating a nested iterable](#creating-a-nested-iterable)
    - [Nesting between list, tuple, dictionary, and set](#nesting-between-list-tuple-dictionary-and-set)
    - [Accessing items from the nested iterable](#accessing-items-from-the-nested-iterable)
    - [Modifying items of the nested iterable](#modifying-items-of-the-nested-iterable)
    - [Nesting Useful Examples:](#nesting-useful-examples)

# Introduction to nesting
Nesting is the process of creating an iterable inside another iterable.
For example If we add List inside another List, then we call it as a
nested list. We also call nested list as n-dimensional list.
## Creating a nested iterable
A nested List is a list that contains a list. For example:

**Example 1:** Nested Lists and Tuples
```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_tuple = (('a', 'apple'), ('b', 'ball'), ('c', 'cat'))

# we can also represent them multiline to make it more readable.

nested_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
nested_tuple = (
    ('a', 'apple'),
    ('b', 'ball'),
    ('c', 'cat'),
)

```
**Example 2:** Nested dictionary
```python
person = {
    'name': 'John',
    'age': 20,
    'company': {
        'name': 'Microsoft',
        'established': 1974,
        'location': 'Albuquerque, New Mexico'
    }
}
```

## Nesting between list, tuple, dictionary, and set

## Accessing items from the nested iterable

## Modifying items of the nested iterable


## Nesting Useful Examples:
