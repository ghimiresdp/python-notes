# https://sudipghimire.com.np
# %% [markdown]
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
# %%
# creating a set
numbers = {18, 24, 56, 21, 44, 27, 99, 100, 64}
animals = {'cat', 'dog', 'tiger'}
random_lists = {1, 'John', 'Moon', True, 45.62}

# Sets has unique set of data
numbers = {18, 24, 16, 18, 44, 21, 24, 18, 19, 44, 18}

# the result would be {44, 16, 18, 19, 21, 24}

# %%
a = {2, 4, 6, 8, 10}
b = {2, 3, 5, 7}
# %%
# adding an item to the set

a.add(12)

# %%
# adding more elements to the set with update()
# we can use any kind of iterable to update the set
# this method still discards the duplicates without error
a.update([14, 16, 14, 18])  # list
a.update((20, 22))  # tuple
a.update({24, 26})  # set

#%%
# remove an arbitary item from the set
a.pop()

#%%
# removing an item from the set with discard()
# it removes the supplied element if there are any in the set.
# if there is no element that is supplied in an argument, then
# it just ignores the process without throwing an error.
a.discard(18)


#%%
# removing an item from the set with remove()
# it removes the supplied element if there are any in the set. Additionally,
# it throws an error if there is no supplied element in the set
# the exception will be key error
a.remove(18)    # less preferred


#%%
# finding the length of the set
print(a.__len__())


#55
# accessing an item of the set is not as simple as of the list or tuple
# we use loops for accessing them
# in other languages, it is also known as for-each loop
# we will discuss more on loop in coming exercises
#%%
for item in a:
    print(item)


#%%
# Mathematics behind the sets

a = {2,4,6,8,10}
b = {2, 3,5,7}

# union [A u B]

print(a.union(b))

# intersection [A n B]
a.intersection(b)   # or
b.intersection(a)

# difference [A only] or [A - B]
a.difference(b)

# symmetric difference [A only] u [B only]
a.symmetric_difference(b)

# More set Methods

"""
You can practice these methods of sets
- clear()           -> clears everything fronm the set
- copy()            -> copies all elements of the set to another variable
- isdisjoint()      -> it checks if 2 sets are distinct or not
- issubset()
- issuperset()
...
"""

"""
- a is a subset of b is a contains all elements of b and probably more
- `b` is `a` superset of `a` if `a` is `a` subset of `b`
- if a is a subset of b then b is a subset of a only if a and be has the same elements inside them

"""


# %%
# d = a vs d = a.copy()

# d = a
# assignment statement in python do not copy objects, but create a binding between target and the source.
# it has the reference if a in the variable d instead of copying the whole object.
# here, changing `a` will affect the value in `d`

# d = a.copy()  # shallow copy
# it constructs a new compound object and then (to the extent possible) inserts references into it
# to the objects found in the original.
# once the value is changed in in any of them, it is not reflected in this case.
# changing `a` will not affect the value in `d`
# for more detail about shallow copy, please check https://docs.python.org/3/library/copy.html


a = set(range(0, 12))
b = set(range(5, 13))

