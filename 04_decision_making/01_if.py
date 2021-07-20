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
a = 20
b = 25
if a < b:
    print(f'{a} is less than {b}')

# %% [markdown]
"""
## If else
- if else condition is same as if condition
- we use else for the condition that does not satisfy the if condition

Syntax
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

Syntax
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
# <value_1> if <condition> else <value_2>
a = False
x = 5 if a is True else 10
print(x)

# %% <value_1> if <condition_1> else <value_2> if <condition_2> else <value_3?
a = 11
x = 'small' if a < 10 else 'medium' if a == 10 else 'large'
print(x)
