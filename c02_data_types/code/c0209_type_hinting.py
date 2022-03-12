# %%
# https://sudipghimire.com.np
"""
Type Hinting in Python

- Introduced first in python 3.6
- Hinting is not strict so the statement can contain different datatypes
- Hintings are useful specifically for the development purpose rather than execution
- Hintings do not make python statically typed, but adds confidence to the programmers
- it makes programmers productive by hinting the exact data type so that we do not need to browse the source

"""
from typing import Dict, List


# %% Some Examples of hinting in statements

a: int = 5                  # same as a = 5

x: str = "ssdsd"

b: float = 5.5              # same as b = 5.5
c: str = 'Tyrion Lannister'
d: list = [1, 2, 3, 4, 5, 'abc']
e: tuple = (1, 2, 3)

# List<int>

# %% Compound Types
import typing
from typing import List
l1: List['int'] = [4, 5]


l2: List = ['abc', 45]

d1: Dict[str, str] = {'k': 'v'}


# these are the basic Type hintings.
# Creating custom types will be discussed in the python L2 course since
# this part requires the knowledge of classes and inheritance

import math
def add_int(x, y):
    
    return( math.floor(x) + y)
