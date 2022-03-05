# © https://sudipghimire.com.np
# %% [markdown]
"""
## List Comprehension
List Comprehension creates a new list by applying an expression to each element
of an iterable.


Basic Syntax:
[<expression> for <element> in <iterable>]

With if condition:
[<expression> for <element> in <iterable> if <condition>]

"""
# %% creating a square of numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# regular method
result = []
for x in numbers:
    result.append(x ** 2)

# list comprehension
result = [x ** 2 for x in range(1, 11)]
print(result)

# %%
# multiplying each value of a list by 3
numbers = [1, 45, 6, 23, 89, 2, 78, 41]
result = [x * 2 for x in numbers]
# %% conditions inside list comprehension
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# I want y to be odds
# and z to be evens

y = [y for y in x if y % 2 == 0]
z = [y for y in x if y % 2 != 0]
print(y)
print(z)

# %%
"""
Creating a multi-dimensional list [[1,2,3],[1,2,3],[1,2,3]]
"""
# %% Step 1, visualize with traditional loop
outer = []
for x in range(1, 4):
    # some other non-related expressions are not used
    inner = []
    for y in range(1, 4):
        inner.append(y)
    outer.append(inner)
print(outer)

# %% step 2 replace inner loop with list comprehension
outer = []
for x in range(1, 4):
    inner = [y for y in range(1, 4)]
    outer.append(inner)
print(outer)

# %% step 3 simplify the inner loop

outer = []
for x in range(1, 4):
    outer.append([y for y in range(1, 4)])
print(outer)
# %% step 4, replace the outer loop with list comprehension

outer = [[y for y in range(1, 4)] for x in range(1, 4)]
print(outer)

# %% example 2, 3d list
"""
Expected list
[
    [[1,2], [1,2]],
    [[1,2], [1,2]]
]
"""
outer = [[[z for z in range(1, 3)] for y in range(1, 3)] for x in range(1, 3)]
print(outer)

# %%
lst = [1, 2, 3, 4, 5]
# I want output to be [1, 4, 9, 16, 25]
new_lst = []
for x in lst:
    new_lst.append(x ** 2)
lst = new_lst
print(lst)

# %% with list comprehension
lst = [1, 2, 3, 4, 5]
lst = [x ** 2 for x in lst]
print(lst)
