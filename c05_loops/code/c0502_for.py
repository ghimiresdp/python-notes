# © https://sudipghimire.com.np
# %% [markdown]
"""
## For Loop
- it is different than for loops in other programming languages.
- for loop in python is similar to for each loop in other languages.
- it iterates over the iterable such as list, tuple, etc.

in other programming languages we have the following syntax
for(<assignment>; <condition>; <update>)
for (int x =0; x<10; x++){
    // sdsd
}
# for python
for <element> in <iterable>:
    statement(s)
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
for i in range(10):
    if i == 5:
        continue
    if i == 8:
        break
    print(f'current value of x is {i}')
print('loop complete')

# %%
for x in range(10):
    x += 1
    # These lines do not fulfill else condition in while else
    # if x == 5:
    #     continue
    # print(f'current value of x is {x}')
    # if x == 8:
    #     break
else:
    print(f'x is now {x}, now Exiting!!')
