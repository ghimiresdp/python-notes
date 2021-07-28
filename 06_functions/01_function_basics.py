# © https://sudipghimire.com.np
# %% [markdown]
"""
Functions
- block of code that runs when it is called
- takes zero or more parameters as arguments
- returns zero or 1 value
- if we want to return more than one value, it returns as tuple
- declared using `def` keyword
- used for reducing duplicates
- modular approach
- it can have any type of arguments integers, floats, lists, even functions
- it can have zero arguments too.

Basic structure
def <function_name> (arg1, arg2, .., argn):
    # statements (always indented)

"""


# %% function definition

def my_function():
    print("Inside the Function")


print("Outside the function")

# %% Calling a function
my_function()


# %% function with parameters or arguments
# adding two numbers

def add_me(a, b):
    # c = a + b
    # return c
    return a + b


add_me(2, 3)

# %% inbuilt print() function

print("Aashish", end=' --->')
print("Roshan")

print("Aashish", "Mohammad", "Roshan", sep=' > ')


# %% the `return` statement
# AddMe()   # valid but not recommended
# addMe()   # valid but not recommended
# Add_Me()   # valid but not recommended

# return statement ends the function
# any statement that is written after the statement is going to be ignored
#  it is never going to be executed
# we can not have more than one return statement in the same indent level
# always use return statement at the end of the function
def add_me2(a, b):
    print(f"I have added{a} and {b}")  # it never executes
    c = 4 + 5
    d = 9 - 3
    return a + b


x = add_me2(2, 3)


# %% the `pass` statement


def add():
    # todo 2021-08-01
    pass


def subtract():
    pass


def multiply():
    pass


def divide():
    pass


# %% different returns in different cases


def check_number_plate(number):
    if number % 2 == 0:
        return 0
    else:
        return 'This vehicle is allowed'


print(check_number_plate(4443))
print(check_number_plate(4444))

