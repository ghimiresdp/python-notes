# © https://sudipghimire.com.np
# %% [markdown]
"""
If Condition
- It is written with `if` keyword
- all the conditions that are enclosed within the `if` statement are
  indented.
- Unlike other programming languages, it do not need curley brackets
  or braces and might not need brackets for simple logical operations
- to end the statements inside of if condition, we just un-indent it

Syntax
```
if <condition>:
    <statements>
```
"""
# %%
a = 20
b = 25
if a > b:
    print(f'{a} is less than {b}')
print('dummy line')

# %% [markdown]
"""
## If else
- if else condition is same as if condition
- we use else for the condition that does not satisfy the if condition

Structure
```
if <condition>:
    <statements>
else:
    <alternative statements that does not satisfy if condition>
```
"""
x = 5

if x % 2 == 0:
    print(f'{x} is even number')
else:
    print(f'{x} is odd number')

# %% [markdown]
"""
## If elif else
- elif contains multiple conditions.
- if previous condition fail and we still need condition in the alternative conditions we can use
  elif.
- we can use any number of elif conditions in python.

Structure
```
if <condition>:
    <statements>
elif <alternative condition>:
    <alternative statements that satisfies elif>
else:
    <statements that does not satisfy any of above>
```
"""
x = 6
if x < 5:
    print(f'{x} is less than 5')
elif x == 5:
    print(f'{x} is equal to 5')
else:
    print(f'{x} is greater than 5')

# %%  if else as one liner assignment
# They are also called as ternary operators
# <value_1> if <condition> else <value_2>
a = False
x = 5 if a is True else 10
print(x)
# %%
a = 11
x = 'even' if a % 2 == 0 else 'odd'

print(x)

# I have a note of <> amount.
# I need to give it to Mohammad if
# it is greater than 100, and Roshan if it is less than 100
amount = 50

# Receiver is Mohammad if amount is greater than 100 else Roshan
receiver = 'Mohammad' if amount > 100 else 'Roshan'

"""
# The regular condition would be
if amount > 100:
    receiver = 'Mohammad'
else:
    receiver = 'Roshan'
"""

# %% <value_1> if <condition_1> else <value_2> if <condition_2> else <value_3?
a = 11
# The regular condition would be
if a < 10:
    x = 'small'
elif a == 10:
    x = 'medium'
else:
    x = 'large'

x = 'small' if a < 10 else 'medium' if a == 10 else 'large'

print(x)

# %%
a = 'Brazil'
# The regular condition would be
if a == 'Brazil':
    continent = 'Americas'
elif a == 'Spain':
    continent = 'Europe'
else:
    continent = 'Asia'

continent = 'Americas' if a == 'Brazil' else 'Europe' if a == 'Spain' else 'Asia'

print(continent)
