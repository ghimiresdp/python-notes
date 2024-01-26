# Chapter 5.2: For Loop

**Table of Contents**:

- [Chapter 5.2: For Loop](#chapter-52-for-loop)
- [Introduction to For Loop](#introduction-to-for-loop)
  - [The Range Function](#the-range-function)
  - [Using For loop with string, list, tuple, set, and dictionary](#using-for-loop-with-string-list-tuple-set-and-dictionary)
  - [Nested For Loop](#nested-for-loop)
  - [The `enumerate()` function](#the-enumerate-function)
  - [The `zip()` function](#the-zip-function)

# Introduction to For Loop

A For Loop iterates over a sequence of items over the iterable in the order that they appear in a sequence.
While `while` loops generally use the conditions for breaking out of the loop, `for` loops have definite number of items
to iterate over. Generally, We use generator function (eg: `range()`) to create a sequence of numbers and loop over them
to achieve loop for n-times.

## The Range Function

The `range()` function creates a range of numbers through which, we can iterate over using for loop. The `range()`
function is a generator which *yields* an item at a time rather than returning the whole sequence of numbers which saves
a lot of memory when generating a sequence of millions of items.

**Example 1:**

```python
range(10)  # creates a range from 0 upto 9
range(1, 10)  # creates a sequence of numbers from 1 to 10
range(1, 10, 2)  # createa a sequence of numbers from 1 to 10 with step of 2
```

**Example 2:** Using `range()` function to iterate for 10 times

```python
for x in range(10):
    print(f'The current value of x is: {x}')
```

**Output**

```
The current value of x is: 1
The current value of x is: 2
The current value of x is: 3
The current value of x is: 4
The current value of x is: 5
The current value of x is: 6
The current value of x is: 7
The current value of x is: 8
The current value of x is: 9
```

**Example 3:** different usage of `range()` function.

```python
# generating odd numbers from 1 upto 19
odd = list(range(1, 20, 2))
print(odd)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# Generating multiples of 3
multiples = list(range(3, 31, 3))
print(multiples)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

```

## Using For loop with string, list, tuple, set, and dictionary

**Example 1:** For Loop with String

```python
name = 'Hello World!'
for char in name:
    print(f'Ascii value of [ {char} ]: ', ord(char))
```

**Output:**

```
Ascii value of [ H ]:  72
Ascii value of [ e ]:  101
Ascii value of [ l ]:  108
Ascii value of [ l ]:  108
Ascii value of [ o ]:  111
Ascii value of [   ]:  32
Ascii value of [ W ]:  87
Ascii value of [ o ]:  111
Ascii value of [ r ]:  114
Ascii value of [ l ]:  108
Ascii value of [ d ]:  100
Ascii value of [ ! ]:  33
```

**Example 2:** For Loop with List / tuple / set

```python
odd = [1, 3, 5, 7, 9]
double_odd = []
for num in odd:
    double_odd.append(2 * num)
print(double_odd)

# Output: [2, 6, 10, 14, 18]

even = (2, 4, 6, 8, 10)
for num in even:
    print(num, end=' ')

# Output: 2 4 6 8 10


prime = {2, 3, 5, 7, 11}
for num in prime:
    print(num, end=', ')

# Output: 2, 3, 5, 7, 11
```

**Example 3:** For loop with dictionary

```python
person = {
    'name': 'Spock',
    'age': 90,
    'address': 'Vulcan'
}

for key, value in person.items():
    print(f'The {key} is {value}')
```

**Output:**

```
The name is Spock
The age is 90
The address is Vulcan
```

## Nested For Loop

**Example 1:**

```python
nested = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for x in nested:
    for y in x:
        print(y, end=' ')

# Output: 1 2 3 4 5 6 7 8 9
```

**Example 2:**

```python
lang = {
    'low level': ['Machine Level', 'Assembly'],
    'high level': ['C++', 'Java', 'Python']
}

for lang_type in lang:
    for lng in lang[lang_type]:
        print(f'The {lang_type} programming language is {lng}')
```

**Output:**

```
The low level programming language is Machine Level
The low level programming language is Assembly
The high level programming language is C++
The high level programming language is Java
The high level programming language is Python
```

## The `enumerate()` function

The `enumerate()` function enumerates the value of an iterable with the index of that item. example if we have a
list `['a', 'b', 'c', 'd', 'e']`, then the `enumerate()`
function gives the tuple of the index of the list and the item on typecasting.

**Example:**

```python
items = [chr(val) for val in range(65, 70)]  # convert ASCII value to character
print(items)
# ['A', 'B', 'C', 'D', 'E']

print(list(enumerate(items)))
# [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]
```

We can also use for loop within `enumerate()` function

**Example:**

```python
casts = ['Robert Downey Jr.', 'Scarlett Joahnsson', 'Chris Evans', 'Mark Ruffalo', 'Chris Hemsworth']

for index, cast in enumerate(casts):
    print(f'{index})\t{cast}')
```

**Output:**

```
0) Robert Downey Jr.
1) Scarlett Joahnsson
2) Chris Evans
3) Mark Ruffalo
4) Chris Hemsworth
```

## The `zip()` function

The `zip()` function also does something similar to the `enumerate()` function but requires 2 or more set of items with
equal length. It zips all the values of same index to a tuple of items.

**Example:**

```python
casts = ['Robert Downey Jr.', 'Scarlett Joahnsson', 'Chris Evans', 'Mark Ruffalo', 'Chris Hemsworth']
characters = ['Iron Man', 'Black Widow', 'Captain America', 'Hulk', 'Thor']

print(list(zip(casts, characters)))
'''
[
    ('Robert Downey Jr.', 'Iron Man'),
    ('Scarlett Joahnsson', 'Black Widow'),
    ('Chris Evans', 'Captain America'),
    ('Mark Ruffalo', 'Hulk'),
    ('Chris Hemsworth', 'Thor')
]
'''

for cast, character in zip(casts, characters):
    print(f'- {cast} played as "{character}" in Avengers')
```

**Output:**

```
- Robert Downey Jr. played as "Iron Man" in Avengers
- Scarlett Joahnsson played as "Black Widow" in Avengers
- Chris Evans played as "Captain America" in Avengers
- Mark Ruffalo played as "Hulk" in Avengers
- Chris Hemsworth played as "Thor" in Avengers
```

We can also zip multiple lists

**Example:**

```python
roll = [1, 2, 3, 4]
name = ['John Lennon', 'John Legend', 'John Mayer', 'John Denver']
songs = ['Imagine', 'All of Me', 'Gravity', 'Take Me home']

for items in zip(roll, name, songs):
    print(items)
```

*Output:**

```
(1, 'John Lennon', 'Imagine')
(2, 'John Legend', 'All of Me')
(3, 'John Mayer', 'Gravity')
(4, 'John Denver', 'Take Me home')
```
