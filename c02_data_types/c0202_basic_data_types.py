# https://sudipghimire.com.np
"""
Numeric Data Types in Python

to run the file, we can go to the terminal and just type
python 02_data_types/02_basic_data_types.py

"""
x: complex = -5j
x = 5  # integer
x = 5.5  # float
x = True  # Boolean

# simple interest
# p -> principal amount         10000
# r -> rate                     10.5% oof interest
# t -> time (years)             1.5

p = 10000   # integer
r = 10.5    # float
t = 1.45    # float

print(type(p))

# practice
simple_interest = (p * t * r) / 100
print(simple_interest)


# String Data Types in Python
string_one = 'Hello World'

# Lists
'''
    - They are similar to arrays in other programming languages
    - They are containers for multiple data
    - Items are ordered
    - First index of the list is 0
    - The list with n number of items has last index of n-1

    - Differences between arrays in other programming languages and lists in python are:
        - It can have more than one type of data
            [1, 1, 'a', 1.5, [1,'a'], True]
        - Lists are mutable

    - Lists can have duplicate values
'''

# Initializing a list
# we initialize a list using a large bracket or Square bracket []
# Each item is separated by comma
# It is recommended to use a space after comma
# It is also possible to assign it in multiple lines

list_one = [1, 2, 3, 4, 5]
list_one.append(6)

wild_animals = [
    'Tiger',
    'Lion',
    'Leopard',
    'Elephant',
    'Rhino'
]


# Tuple Data Type

"""
- Tuples are similar as lists, but the values are immutable
    - Tuples are ordered
    - Tuples index starts with 0
    - Tuples can have more than one data types
    - Tuples can be non-unique
    - Tuples can not be changed or modified once initialized
    - We can not add or remove elements from tuple
- Tuples are represented by small brackets.
- Tuples are faster than lists
"""

# initializing a tuple
tuple_one = (1, 2.4, 3, 4, 4, 'Cat', [1, 2, 3])

wild_animals_tuple = ('Tiger', 'Lion', 'Leopard', 'Elephant', 'Rhino')


# Sets
"""
- Sets are similar to lists except they have unique data
- Sets are represented by braces {}
- Sets are not ordered
- Sets can not be accessed with indices.
- Set items can not be changed individually, but can be added to it

- Mathematical operations
    - Union
    - Intersection
    - Difference, ...

"""

# initializing a set

set_one = {1, 2, 3, 4}

set_2 = {1, 2, 3, 4, 4}

print(set_2)
