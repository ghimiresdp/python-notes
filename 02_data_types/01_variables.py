# https://sudipghimire.com.np
"""
Variables in Python

let us suppose we have a statement as follows:
x = 5

here, `x` is a variable.
The word used in a variable is also known as identifier
"""

a = 5  # integer
b = 5.45  # floating point numbers (floats)
c = "Hello There+-!#$....."  # string

#   the keyword = is used for assignment

# statement
x = a + 10  # x = 15

x = x + 1  # x = 16
# It might be confusing to people when we see `x = x+1` in the statement since it mathematically
# violates the left hand and right hand values. We can think `=` as the update to the previous value, which makes it
# visually similar to `x <- x+1` or x is updated to be x + 1 from now onwards


# defining multiple variable at once in python
# let us suppose we have 3 variable declarations
v1 = 5
v2 = 6
v3 = 7
# we can achieve it in the single line with the following statement
v1, v2, v3 = 5, 6, 7

# or
(v1, v2, v3) = (5, 6, 7)


# rules for defining an identifier (name of the variable)

"""
1. it can start with alphabetical characters
2. it can start with _ character
3. it can have numeric characters in between or at the end but not in the beginning
4. we can not use special characters like space, tab, `+`, `-`, etc.
5. we can separate different words with underscores `_`
6. we use snake_case for variable definition

lists of valid and invalid identifiers are shown below:

1.      name = 'cow'        -> Valid
2.      Name = 'cow         -> Valid but not recommended by PEP (Always use snake case)
3.      name one = 'cow'    -> Invalid since it can not contain special characters except `_`
4.      1name = 'cow'       -> Invalid since it can not start with numeric characters
5.      name1 = 'cow'       -> Valid
6.      name_1 = 'cow'      -> Valid
7.      first_name = 'John' -> Valid
8.      FirstName = 'John' -> Valid bud not recommended by PEP (Camel case is recommended for classes)
"""
