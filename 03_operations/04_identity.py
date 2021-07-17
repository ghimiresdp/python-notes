# https://sudipghimire.com.np
"""
Identity operations
- used to compare whether they are same object or not
- they are not used to compare for equality
- identity operators are:
    1. `is`
    2. `is not`
"""

# %% The right method

print(type('abc') is str)   # True

list1 = ['abc', 'def']
list2 = list1           # same object is referenced here
list3 = list1.copy()    # shallow copy is made here

print(list1 is list2)   # True

# == is not same as is
print(list1 is list3)   # False
print(list1 == list3)     # True

print(type(list1) is not int)  # True


# %% the wrong method
print(1 + 4 is 6-1)
# this gives equality but it shows warning to use  double equals
# rather than `is` since it is not intended to compare

# %%
# We will be dealing with identity operator when we
# start object oriented programming
