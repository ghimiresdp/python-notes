# https://sudipghimire.com.np
# %% [markdown]
"""
# Bitwise Operators

- bitwise operators, as suggested by name, work on bit.
- bitwise operator works only with numeric values
- operation is done with each bit position rather than the value as a whole
- suppose we have 2 numbers `5` and `6`
We need to understand binary to decimal conversion and vice versa to understand bitwise operation

binary numbers are also known as base-2 numbers

** not just valid for python

- `5` in decimal is `101` in binary
- `16` in decimal is `10000` in binary

for uint8 or u8,

5   =   0 0 0 0    0 1 0 1
16  =   0 0 0 1    0 0 0 0

for uint32 or u32,

5   =   `0000 0000 0000 0000 0000 0000 0000 0101`

16  =   `0000 0000 0000 0000 0000 0000 0001 0000`

in the above example, we perform bitwise operation to same positioned digit
of the both numbers
    - the first digit of the first value interacts with the first digit of second value
    - the second digit of the first value interacts with the second digit of second value,
      ...
    - the last digit of the first value interacts with the the last digit of second value

you can always check the binary value of a number with
`bin()` function.


Some Bitwise Operations

- Bitwise AND operator `&`
- Bitwise OR operator `|`
- Bitwise NOT operator `~`
- Bitwise XOR operator `^`
- Bitwise SHIFT LEFT operator `<<`
- Bitwise SHIFT RIGHT operator `>>`


"""

# %% Bitwise AND operator `&`

'''
Here 5 is 101 and 6 is 110
Starting from the last digit of both 5 and 6,
we do bitwise AND Operation
Bitwise means,
'''
x = 5            # 0 0 1 0 1
y = 21           # 1 0 1 0 1
print(x & y)     # 0 0 1 0 1    5

# job married children
#   1   0   0
# 4
# %% Bitwise OR operator `|`

x = 5            # 0 0 1 0 1
y = 16           # 1 0 0 0 0
print(x | y)     # 1 0 1 0 1    21

# %% Bitwise NOT operator `~`

x = 5            # 0 1 0 1
print(~5)        # 1 0 1 0

# %% Bitwise XOR operator `^`

