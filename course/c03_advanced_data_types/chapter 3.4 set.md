- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

[go to course contents](https://github.com/ghimiresdp/python-level1/)
-----------------------

# Chapter 3.4. Set

**Table of Contents**

- [Chapter 3.4. Set](#chapter-34-set)
    - [Introduction](#introduction)
    - [Creating a set](#creating-a-set)
    - [Adding an item to the set](#adding-an-item-to-the-set)
    - [Adding multiple items to the set](#adding-multiple-items-to-the-set)
    - [Removing items from the set](#removing-items-from-the-set)
    - [finding out the length of the set](#finding-out-the-length-of-the-set)
    - [Mathematical model of the set](#mathematical-model-of-the-set)
        - [Union](#union)
        - [Intersection](#intersection)
        - [Difference](#difference)
        - [Symmetric Difference](#symmetric-difference)
    - [Accessing items of a set](#accessing-items-of-a-set)
    - [Some useful Set Methods](#some-useful-set-methods)
    - [Practical Implementation: removing duplicate of a list](#practical-implementation-removing-duplicate-of-a-list)

## Introduction

Sets are similar to lists except they can contain unique items. Some features of sets are as follows.

- Sets are similar to lists except they have unique data
- Sets are represented by comma separated values enclosed within braces `{}`
- Sets are not ordered, so we can not access sets using indices.
- Set items can not be changed individually, but can be added to it or removed from it.

## Creating a set

As explained above, sets can be created using comma separated values enclosed within braces.

**Example:**

```python
numbers = {18, 24, 56, 21, 44, 27, 99, 100, 64}
animals = {'cat', 'dog', 'tiger'}
random_lists = {1, 'John', 'Moon', True, 45.62}
```

If we create a set with duplicate values, they get discarded.

```python
numbers = {18, 24, 16, 18, 44, 21, 24, 18, 19, 44, 18}
print(numbers)

# {44, 16, 18, 19, 21, 24}
```

## Adding an item to the set

we can add an item to the set using `set.add()` method.

```python
prime = {2, 3, 5, 7}
prime.add(11)
print(prime)
# {2, 3, 5, 7, 11}
```

## Adding multiple items to the set

We can add multiple items to the set using `set.update()` method. The `update()`
method takes an iterable which might be a list, tuple, set, or any iterable.

```python
prime = {2, 3, 5, 7}
prime.update([11, 13, 17])
# {2, 3, 5, 7, 11, 13, 17}
```

## Removing items from the set

We can use either of the following methods to remove items from the set:

- `set.discard()` method
- `set.remove()` method

```python
even = {2, 4, 6, 8, 10, 12}
even.discard(12)
print(even)
# {2, 4, 6, 8, 10}

even.remove(10)
print(even)
# {2, 4, 6, 8}
```
Here removing an item with either of the method gives the same result, however
if an item does not exist in the set then the `remove()` method throws a
KeyError.

```python
even = {2, 4, 6, 8, 10}
even.discard(12)

even.remove(12) # KeyError: 12
```

## finding out the length of the set

## Mathematical model of the set

### Union

### Intersection

### Difference

### Symmetric Difference

## Accessing items of a set

We can not access individual item of the set, however we can iterate through all items of a set using for loop.

```python
prime = {2, 3, 5, 7, 11, 13, 17}

for item in prime:
    print(prime)
```

## Some useful Set Methods

- `set.clear()`
- `set.copy()`
- `set.isdisjoint()`
- `set.issubset()`
- `set.issuperset()`

## Practical Implementation: removing duplicate of a list
