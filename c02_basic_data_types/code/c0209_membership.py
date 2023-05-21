# https://sudipghimire.com.np
# %% [markdown]
"""
# Python Membership Operations

Operators:

- Membership operators are used to check if the element is present in the specified object or not.
- basic membership operators:
    - `in` (format: `a in x`)
    - `not in` (format: `a not in x`)
- membership operators return either `True` or `False`

"""
# %% `in` operator

x = [1, 2, 3, 4, 5]

print(5 in x)   # True
print(10 in x)  # False

people = ['John', 'Jane', 'Janet']

print('John' in people)         # True
print('Mohammad' in people)     # False


# %% `not in` operator
# this is just opposite of `in` operator
print('John' not in people)     # False

print(5 not in x)   # False
print(10 not in x)  # True
