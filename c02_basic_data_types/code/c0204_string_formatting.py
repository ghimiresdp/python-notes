# https://sudipghimire.com.np
"""
Formatting Strings in Python

Formatting strings:
- %s
- %<a>d     (Used for numeric values)
- %<a>.<b>f (Used for floating point values)
- `format()` function
- `format()` function with parameters
- f-strings

"""

# formatting with %s, and %d
# print("Enter your name: ", end='\t')
# name = input()

# print("Enter your age: ", end='\t')
# age = int(input())
import math

name = 'John Doe'
age = 25

formatted_string = 'My name is %s. I am %d years old !!' % (name, age)
print(formatted_string)  # My name is John Doe. I am 25 years old !!

# Formatting with `%<a>d` and `%<a>.<b>f`
# a -> total number of characters expected.
#       - If the number has less than `a` number of characters, it is going to add padding with space before number
#       - If the number can not be represented with only `a` number of characters, it is going to ignore the number `a`
# b -> number of characters expected after the decimal point.
#  45.335

print("the value is:%10.3f" % 44.2345345)  # output:    44.235
print("the value is:%10.3f" % 2244.3234234)  # output:  2244.323
print("the value is:%10.3f" % 23423423.234234)  # output:23423423.234 (it uses more than 10 characters here)
print("the value is:%10d" % 234234)  # output:   234234

# `format() method`
"""
1. format() method uses special templating with braces `{}`.
2. the number of parameters in the method should be exactly equal to the number of pairs of braces in the string
    example: "Hello there, I am {} and I am currently {}" expects exactly 2 parameters in the `format()` function
"""

# suppose we append strings with the following method in string concatenation process.
print("Hi " + name + ", how are you doing? Are you " + str(age) + " now?")

# but with `format()` method, we can easily achieve the same output as follows:

print("Hi {}, how are you doing? Are you {} now?".format(name, age))
# output: Hi John Doe, How are you doing? Are you 25 now?

# Note: the parameters in the method should be in order to properly format the string
print("Hi {}, how are you doing? Are you {} now?".format(age, name))
# output: Hi 25, How are you doing? Are you John Doe now?


# format() with named arguments
"""
In case of formatting with named arguments,
the output will be similar except the parameters do not need to be in order.
"""

print("Hi {n}, how are you doing? Are you {a} now?".format(n=name, a=age))
# output: Hi John Doe, How are you doing? Are you 25 now?

print("Hi {n}, how are you doing? Are you {a} now?".format(a=age, n=name))
# output: Hi John Doe, How are you doing? Are you 25 now?

# f-strings
"""
1. f-strings are also known as formatted strings.
2. we can initialize f-string by typing f just before a string literal.
    eg: f_string_1 = f'my content is here'
    - we can use f-string for strings with both single and double quotes
3. f-strings have syntax similar to format() with named parameters but the statements are directly
    used instead of parameters.
"""

formatted_string = f"Hi {name}, how are you doing? Are you {age} now?"
# output: Hi John Doe, How are you doing? Are you 25 now?

# we can even use complex expressions like
print(f'The word {name} has {name.__len__()} characters')

# or
print(f'The word {name}  is {"long" if name.__len__() > 10 else "short"}')
