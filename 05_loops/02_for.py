# © https://sudipghimire.com.np
# %% [markdown]
"""
## For Loop
- it is different than for loops in other programming languages.
- for loop in python is similar to for each loop in other languages.
- it iterates over the iterable such as list, tuple, etc.
"""

# %% basic syntax
singers = ['John Lennon', 'John Mayer', 'John Legend']
for singer in singers:
    print(f'singer is {singer}')

# %% for loop in range

for x in range(10):
    print(f'the value is {x}')

# %% looping through letters in a string

for char in 'Elephant':
    print(f'the character is: {char}')

# %% we can use break, continue, and else statements in for loop too
