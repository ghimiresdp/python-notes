# https://sudipghimire.com.np
"""
Sets

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

# creating a set
numbers = {18, 24, 56, 21, 44, 27, 99, 100, 64}
animals = {'cat', 'dog', 'tiger'}
random_lists = {1, 'John', 'Moon', True, 45.62}

# Sets has unique set of data
numbers = {18, 24, 16, 18, 44, 21, 24, 18, 19, 44, 18}

# the result would be {44, 16, 18, 19, 21, 24}

# adding an item to the set

numbers.add(5)


# adding more elements to the set with update()
# this method still discards the duplicates without error



# remove an arbitary item from the set
numbers.pop



# removing an item from the set with discard()



# finding the length of the set



# accessing an item of the set is not as simple as of the list or tuple
# we use loops for accessing them
# in other languages, it is also known as for-each loop
# we will discuss more on loop in coming exercises

for item in numbers:
    print(item)


# Mathematics

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

# union [A u B]



# intersection [A n B]



# difference [A only] or [A - B]



# symmetric difference [A only] u [B only]



# More set Methods

"""
You can practice these methods of sets
- add()
- clear()
- copy()
- discard()
- isdisjoint()
- issubset()
- issuperset()
...
"""
