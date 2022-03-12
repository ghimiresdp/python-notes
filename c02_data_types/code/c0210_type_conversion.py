# https://sudipghimire.com.np

"""
Type Conversion
- Type casting or type conversion is the process of converting the data from one
  one type to another.
- We perform type casting to unify the data types for better and efficient calculation

In case of python there are 2 types of type conversion

1. Implicit type casting
    - it is automatically converted by the interpreter while performing calculation
    - it is done when we perform operations between lower and higher precision quantities.
    - Implicit type casting always casts lower precision data type to higher precision one.
    - example: int can be implicitly type casted to float

2. explicit type casting
    - it is a manual process where we want to convert one type of data to another
    - it is more useful when we want to convert numeric to non-numeric and vice-versa.
    - type casting from higher precision data-types to lower-precision data types can also
      lead to the data loss. so we have to make sure that we actually need to convert the
      current data type.
      example: float to int type casting omits all numbers after the decimal.

"""

# %% Implicit Type Casting Example
from typing import Type


x = 5
y = 10.5
print(x+y)  # here interpreter automatically casts x from 5 to 5.0
# in case of other programming languages we might have to
# convert the integer type data to floating poing before
# performing such operations.

# %% Explicit Type Casting
# integer to float type casting

x = 5          # x is int (5)
x = float(x)    # x is float (5.0)
print(type(x))

# %% integer to string
x = 5          # 5
x = str(5)      # '5'
print(type(x))

# %% string to integer

x = "45"
x = int(45)
print(type(x))

# %% string to float

PI = "3.1415"
PI = float(PI)
print(type(PI))

# %% trying to convert incompatible data type gives us value error
PI = "3.1415"
PI = int(float(PI))    # gives Value Error

# %% we can always check if it can be typecasted

PI = "3.1415"
if PI.isdigit():  # it checks if PI is int or not
    PI = int(PI)
else:
    PI = float(PI)
print(type(PI))
# %%

x = [5.7, 8.12, 6, 18, 12.99, 45.86, 33.44]

# no type casting
result = 0
for a in x:
    result = result + a
print(result)

# typecasting in the loop
result = 0
for a in x:
    result = result + int(a)
print(result)

# typecasting in the result
result = 0
for a in x:
    result = result + a
print(int(result))
# %%
# application 1 : removing the duplicates
x = [1, 3, 5, 2, 7, 8, 3, 0, 1, 6, 3, 9, 3]

x = list(set(x))
print(x)


# %%
