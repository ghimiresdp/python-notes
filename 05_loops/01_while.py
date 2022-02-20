# © https://sudipghimire.com.np
# %% [markdown]
"""
## While Loop
- It is used for iterating until the condition fails to satisfy

Basic Syntax:

while <condition>:
    # statements
    <update>

"""
x = 0
while x < 10:
    print(f'current value of x is {x}')
    x += 1
    # x++  # incorrect in case of python

# %% another example
value = 'y'
while value.lower() != 'e':
    value = input('Enter text[`e` to exit]: ')
    print(f'You Entered: {value}')
print('exiting now!!')

# %% another example with numbers

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

# %% printing out only odd numbers below 10
x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x)
print('loop complete')

# %% while else statement
x = 0
while x < 10:
    x += 1
    # These lines do not fulfill else condition in while else
    # if x == 5:
    #     continue
    # print(f'current value of x is {x}')
    # if x == 8:
    #     break
else:
    print(f'x is now {x}, now Exiting!!')

# %% nested loops
"""
1
1 2
1 2 3
1 2 3 4
"""
x = 1
while x <= 4:
    y = 1
    while y <= x:
        print(y, end=' ')
        y += 1
    print()
    x += 1


# While Else
