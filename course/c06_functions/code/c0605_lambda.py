# © https://sudipghimire.com.np
# %%
"""
Python Lambdas
- lambdas are also known as anonymous functions
- they are tiny functions which contains one statement
- lambdas are written in a single line
- they can have zero or more arguments
- they are useful when we have to do small repetitive tasks

structure of lambda
<function_name> = lambda <arg>,<arg>, ...: <return_statement>

- everything before `:` and after `lambda` are arguments
- expression after `:` is the return value
example:
f1 = lambda a,b: a+b
f2 = lambda a: a**2
f3 = lambda : print("Hey There!")
"""


# %% regular function to add 2 numbers and return value

def add_numbers(a, b):
    return a + b


add_numbers(4, 5)

# %% same operation with lambda

add_num = lambda a, b: a + b
add_num(4, 5)

# %%
# multiply 2 numbers
a = 6
b = 8
e = 10

multiply = lambda c, d: c * d + e

multiply(a, b)
# %% lambda with no arguments


print_hello = lambda: print("hello world")
print_hello()

# %% conditionals inside lambda

# ternary operator "Even" if x % 2 == 0 else 'Odd'

odd_even = lambda x: "Even" if x % 2 == 0 else 'Odd'

print(odd_even(14))

# %% double the list
lst = [1, 2, 3, 4, 5]

double1 = lambda l: [x * 2 for x in l]

double1(lst)

lst = [x * 2 for x in lst]
