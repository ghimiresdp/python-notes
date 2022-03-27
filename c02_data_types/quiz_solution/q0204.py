"""
© https://sudipghimire.com.np


Assign a variable  pi and assign value 3.14159265

a. use formatting strings to show pi with 3 digits after the decimal
b. use formatting strings to show pi with 2 digits after the decimal but
    allocate 10 spaces for the variable
c. use f-string to show the result in the following format:
    "The value of PIE is        3.14"

    hint: "%<a>.<b>f"
"""

PI = 3.14159265

# a
print(f"{PI: 5.3f}")

# b
print(f"{PI: 10.2f}")

# c
print(f"The value of PIE is{PI: 12.2f}")
