# https://sudipghimire.com.np
# %%[markdown]
"""
# Tuples
## hubheading 1
sdsdsd

## subheading 2
sdsdsd

1. Tuples are similar to lists  except they are immutable
    - Tuples are ordered
    - Tuples index starts with 0
    - Tuples can have more than one data types
    - Tuples can be non-unique
    - Tuples can not be changed or modified once initialized
    - We can not add or remove elements from tuple

2. Tuples are represented by small brackets() instead of []
3. Tuples are faster than lists

"""

# %%
# Creating a tuple
numbers = (18, 24, 56, 21, 44, 27, 99, 100, 64, 44,)

animals = ('cat', 'dog', 'tiger')
random_tuples = (1, 'John', 'Moon', True, 45.62)

# %%
# similar to lists, new line do not terminate the statement until it finds closing bracket
animals = (
    'cat',
    'dog',
    'tiger'
)

# %%
# tuple with only one item
x = (1,)  # comma is mandatory for tuple with only one element

# %%
# accessing an item of a tuple
print(numbers[1])

# %%
# accessing an item of a tuple with reverse index
numbers[-1]
# %%

# Updating values in a tuple gives an error
# numbers[1] = 5      # gives error

# %%
# if we want to add values to the tuple, we can re assign the value by adding it to another tuple
tuple_1 = (4, 5, 6)
tuple_2 = (7, 8, 9)
tuple_1 = tuple_1 + tuple_2
print(tuple_1)

# %%
# next approach (destructuring)
tuple_1 = (*tuple_1, 10, 11, 12)

print(tuple_1)

"""
 Significance of * in python iterables
 `*<iterable>` -> extract all of those elements and return every
  elements as the individual one
  The process is also known as destructuring

  Destructuring can be used with:
  - lists eg: `*[1,2,3]` or `*list_one`
  - tuples eg: `*(1,2,3)` or `*tuple_one`
  - sets  eg: `*{1,2,3}` or `*list_one`

  We can use destructured elements to:
  - dynamically pass arguments to the function eg: do_something(*args)
  - concatenate two iterables eg: nex_list = [*list_1, *list_2]
  - add extra item while returning the reponse to the client. (We'll deal with this on python level 2)
"""

# %%

# finding the length of the tuple
print(numbers.__len__())
# %%
# nested tuples

nested = ((1, 2), (3, 4), (5, 6))
# %%
# accessing an item of the nested tuple

print(nested[0][0])  # 1 expeted
# %%

# foreach in tuples
for animal in animals:
    print(animal)

# %%
# enumerating the lists
# enumerate keyword
enum = enumerate(numbers)
for (index, number) in enum:
    print(f'{index} - {number}')

# %%
# bonus del keyword (unrelated to tuple)
# we can unassign any variable from the memory with del keyword
# if you want to use the variable after del , then it throws an exception saying
# name `<name_of_variable>` is not defined
del numbers
# %%
