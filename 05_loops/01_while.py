# © https://sudipghimire.com.np
# %% [markdown]
"""
## While Loop
- It is used for iterating until the condition fails to satisfy
"""
x = 0
while x < 10:
    print(f'current value of x is {x}')
    x += 1

# %%
value = 'y'
while value.lower() != 'e':
    value = input('Enter text[`e` to exit]: ')
    print(f'You Entered: {value}')
print('exiting now!!')

# %% infinite loop:
# while True:
#     print('This loop does not end')

# %% break and continue statements in a loop
x = 0
while x < 10:
    x += 1
    if x == 5:
        continue
    if x == 8:
        break
    print(f'current value of x is {x}')
print('loop complete')

# %% while else statement
x = 0
while x < 10:
    print(f'current value of x is {x}')
    x += 1
else:
    print(f'x is now {x}, now Exiting!!')
