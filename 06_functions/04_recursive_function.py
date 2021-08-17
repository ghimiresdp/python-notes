# © https://sudipghimire.com.np
# %%
"""
Recursive Function
- A function that calls itself
- it contains 2 different elements
    - recursion limit
    - next recursion

Basic Syntax

def <function_name>(<depth>):        # depth might be the value to recurse
    if <condition>:
        <function_name>(<updated_depth>)
    else:                           # recursion Limit
        return <final value>
"""


# Program to convert decimal to binary


def dec2bin(n: int):
    if n != 0:
        return dec2bin(n // 2) * 10 + n % 2
    else:
        return 0


print(dec2bin(14))

# %%

"""
1. x = 14

# starts expanding

2. dec2bin(14)
3. dec2bin(dec2bin(7) * 10 + 0)
4. dec2bin(dec2bin(3) * 10 + 1) * 10 + 0)
5. dec2bin(dec2bin(dec2bin(1) * 10 + 1) * 10 + 1) * 10 + 0)
6. dec2bin(dec2bin(dec2bin(dec2bin(0) * 10 + 1 ) * 10 + 1) * 10 + 1) * 10 + 0)

# starts simplifying

7. dec2bin(dec2bin(dec2bin(0 * 10 + 1 ) * 10 + 1) * 10 + 1) * 10 + 0)
8. dec2bin(dec2bin(1 * 10 + 1) * 10 + 1) * 10 + 0)
9. dec2bin(11 * 10 + 1) * 10 + 0)
10. dec2bin(111) * 10 + 0)
10. 111 * 10 + 0)
11. 1110
"""

# %%

"""
similar result without recursion
"""


def dec2bin2(n: int):
    result = []
    next1 = n
    while next1 != 0:
        result.append(str(next1 % 2))
        next1 = next1 // 2
    result.reverse()
    return ''.join(result)


# %%
"""
recursive function to find out factorial of a number

example: 5! = 5 * 4 * 3 * 2 * 1 = 120

"""

# without recursion:

x = 5
result = x
while x > 1:
    result = result * (x - 1)
    x = x - 1
print(result)


# if x = 0 0! = 1
# %% with recursion

def factorial(x: int):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))


# %%
class Customer:
    __logged_in = False

    # decorator function
    def is_logged_in(fn):
        def caller(self, *args, **kwargs):
            if self.__logged_in:
                return fn(self, *args, **kwargs)
            else:
                print("you're not logged in")

        return caller

    @is_logged_in
    def book_trip(self):
        print('trip booked')

    def login(self, username, password):
        if username == 'john' and password == 'p@55w0rd':  # your logic here
            self.__logged_in = True

            print("[ logged in ]".center(60, '='))

            print("Welcome to the dashboard".center(60, ' '))
        else:
            print("invalid credentials...")

    def logout(self):
        self.__logged_in = False
        print("[ logged out ]".center(60, '='))


# %%

john = Customer()
john.book_trip()  # you are not logged in

john.login('jane', 'p@55w0rd')  # logged in
john.book_trip()  # You're not logged in

john.login('john', 'p@55w0rd')  # logged in
john.book_trip()  # Welcome to the dashboard

john.logout()  # logged out
john.book_trip()  # you're not logged in

# %% output
"""
you're not logged in
invalid credentials...
you're not logged in
=======================[ logged in ]========================
                  Welcome to the dashboard
trip booked
=======================[ logged out ]=======================
============================================================
you're not logged in
"""
