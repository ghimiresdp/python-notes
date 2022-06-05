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

## Accessing an item of a list
we can use index of an item inside a large bracket to access an item from the list. The index of the first item starts at `0` and increases as it moves towards the next item.

For example we have a list as follows:

```py
animals = ['cat', 'dog', 'tiger']
```

To access `cat` from the list, we have to write the following statement

```py
# assigning the value to a new variable
x = animals[0]

# printing the value of the item
print(animals[0])
```

We can also use negative index to access index of the list in reverse order.

For example, If we want to access the last item, we can use the index `-1`. Similarly for second last item, we can use the index `-2`.

```py
print(animals[-1])  # tiger
```
