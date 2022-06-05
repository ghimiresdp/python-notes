- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

# Chapter 2.5. Lists

**Ref**: https://docs.python.org/3.9/tutorial/introduction.html#lists

Python list is a compound data type that can store collection of data. List is written as comma separated values/items inside large brackets `[]`.

**Some of the features of list are as follows:**
1. Lists can store multiple items in a single variable
2. Lists are created using Square brackets `[]`
3. Items in list are ordered. i.e. they can be accessed using indexes.
4. The first item of list has index of 0
5. List with n number of items has last index of (n-1)
6. Lists are different than Arrays in other programming languages.
    - lists can have more than one type of data
    - lists are mutable
    - lists do not need data to be unique
    - In python, list items can also be accessed using negative indexes.


## Creating a list

To create a list, we can simply add items separated by comma inside large brackets.

```py
# list of numbers
numbers = [18, 24, 56, 21, 44, 27, 99, 100, 64, 44]

# list of strings
animals = ['cat', 'dog', 'tiger']

# list of multiple data types
random_lists = [1, 'John', 'Moon', True, 45.62]
```

In case of a list, new line do not terminate the statement until brackets are closed.

```py
animals = ['cat', 'dog', 'tiger']

# can also be written as

animals = [
    'cat',
    'dog',
    'tiger'
]
```


