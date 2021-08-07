# © https://sudipghimire.com.np

# %% [markdown]
"""
# `*args` and `**kwargs` parameters in function

- `*args` are  the arbitrary arguments
- `args` can be replaced with any valid identifier for your convenience
- we use `*args` wh
- no. of arguments might be zero or more
"""


# less and definite no. of arguments:

# def add(x, y, z=0):
#     return x + y + z

# generally we write *args
def add(*args):  # a = () -> tuple
    result = 0
    for element in args:
        result += element
    return result


# any number of arguments or any iterables
print(add(1, 2))
print(add(1, 4, 3, 2, 5, 6, 7, 8, 5, 3, 2, 4, 56))
print(add(*range(1, 101)))

# %% Arbitrary number of keyword arguments (**kwargs)

request = {
    'POST': {
        'first_name': 'Aashish',
        'last_name': 'Belbase',
        'license': '123456',
    },

    'GET': {
        'first_name': 'Aashish',
        'last_name': 'Belbase',
        'license': '123456',
    },
    'params': {
        'q': 'sdsdf',
        'oq': 'sdsfdsf',
    },

    'headers': [

    ]
}

req = ['Roshan', 'Maharjan', '78910']


def register_customer(first_name, last_name, license):
    print(f'the first name is {first_name}')
    print(f'the last name is {last_name}')
    print(f'the license number is {license}')


register_customer(
    request['POST']['first_name'],
    request['POST']['last_name'],
    request['POST']['license'],
)

register_customer(**request['POST'])
register_customer(*req)


# %%

def register_customer_1(*args):
    pass


# %%
def register_customer_2(**kwargs):
    print(kwargs)


register_customer_2(**request['POST'])

# %%

add(1, 2)
add(1, 2, 3)
add(1, 2, 3, 4, 5, 6, 7, 8, 9, )


# %%
def print_detail(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = '{value}'")


print_detail(
    book_name="How to learn language",
    price="400",
    author="Roshan",
    co_author="Aashish"
)

# %%
"""
we can use all types of arguments in a single function. i.e.:
- arguments add(a,b)
- keyword arguments  add(a,b,c=0)
- arbitrary arguments add(*args)
- arbitrary keyword arguments add(**kwargs)

But the precedence is:
1. required arguments first,
2. and then default arguments,
3. and then *args,
4. and finally, **kwargs

otherwise function definition gives an error


def fun(a,b=5,c, *args, **kwargs)       # incorrect (required should be first)
def fun(a,b,c, *args, **kwargs, d=5)    # incorrect (*args and **kwargs should be at last)
"""


# %%
def super_add_function(a, b, c=0, *args, **kwargs, ):
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'args = {args}')
    print(f'kwargs = {kwargs}')
    result = a + b + c
    for value in args:
        result += value
    for _, value in kwargs.items():
        result += value

    return result


# for super_add_function(),
# minimum arguments must be 2
# maximum arguments can be any no. of arguments
# default argument will be 1
# we can pass zero to infinite arbitrary arguments
# we can pass zero to infinite arbitrary keyword arguments


# print(super_add_function(1, 2, 3, 4, 5))
# print(super_add_function(1, 2, 3, 4, 5, m=10, n=12))


office = 10
home = 10
misc = [65, 32, 89, 23, 88]
other_expenditure = {
    'bus_fare': 100,
    'pen': 10,
    'gas': 20
}

print(super_add_function(office, home, 0, *misc, **other_expenditure))
