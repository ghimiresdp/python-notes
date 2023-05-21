# © https://sudipghimire.com.np
# %% [markdown]
"""
Functions
- block of code that runs when it is called
- provide organized, reusable and modular code
- used for reducing duplicates
- modular approach
- takes zero or more parameters as arguments
- returns zero or 1 value
- if we want to return more than one value, it returns as tuple
- declared using `def` keyword
- it can have any type of arguments integers, floats, lists, even functions
- unlike other programming languages, python function body can not be empty

example of builtin functions:
- print()
- input()
- len()

Basic structure
def <function_name> (<arg1>, <arg2>, .., <arg_n>,):
    # statement(s) (always indented)
"""


# %% function definition
# AddMe()   # valid but not recommended
# addMe()   # valid but not recommended
# Add_Me()   # valid but not recommended

def my_function():
    print("Inside the Function")


print("Outside the function")

# %% Calling a function
my_function()


# %% function with parameters or arguments
# adding two numbers

def add_me(num_1, num_2):
    print(f'num_1 is {num_1}')
    print(f'num_2 is {num_2}')
    return num_1 + num_2


x = add_me(2, 3)
print(x)

x = add_me(5, 8)
print(x)
x = add_me(num_2=5, num_1=8)
print(x)
print(add_me(5, 7))
print(add_me(-34, 76))


# %% problem 1
# I have to add 3 different numbers
def add(a, b, c):
    return a + b + c


add(4, 6, 8)

# %% inbuilt print() function

print("Aashish", end=' ---> ')
print("Roshan")

print("Aashish", "Mohammad", "Roshan", sep=' > ')


# %% the `return` statement
# return statement ends the function
# any statement that is written after the return statement is going to be ignored
#  it is never going to be executed
# always use return statement at the end of the function if we need to return value(s)
# we can not have more than one return statement in the same indent level

def add_me2(a, b):
    print(f"I have added {a} and {b}")  # it never executes
    return a + b
    c = a * b  # unreachable code
    print(c)  # unreachable code


# example of unreachable code in if condition
if 1 == 2:
    print("1 is equal to 2")  # unreachable code

x = add_me2(2, 3)
print(x)


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
        return 'This vehicle is not allowed'
    else:
        return 'This vehicle is allowed'


print(check_number_plate(4443))
print(check_number_plate(4444))
