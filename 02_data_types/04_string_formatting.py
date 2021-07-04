#%%
"""
Formatting Strings in Python
https://sudipghimire.com.np

Formatting strings:
- %s
- %<a>d
- %<a>.<b>f
- `format()` function
- `format()` function with parameters
- f-strings

"""

#%%
a = "String one"
my_name = "JOhn Doe"

x = "1my_name1"

print(x.isidentifier())



# formatting with %s, and %d
# print("Enter your name: ", end='\t')
# name = input()

# print("Enter your age: ", end='\t')
# age = int(input())

name = 'John Doe'
age = 25

formatted_string = 'So, your Name is %s? cool! %d even cooler !!' % (name, age)
# next_format = 'sdfsdfsdfds f%f'%(formatted_string)
print(formatted_string)


# Formatting with %<a>.<b>
# _ _ 4 5 . 335
# a -> number of characters expected
# b -> number of characters expected after the decimal point.
#  45.335

# 80 characters
some_float = 45.3345447
print("the value is:%18.3f"%(44.2345345))
print("the value is:%18.3f"%(2244.3234234))
print("the value is:%18.3f"%(23423423.234234))
print("the value is:%18d"%(234234))


# `format() method`

print('\n\n\n')

print("Hi " + name + ", how are you doing? are you " + str(age) + " now?")
# same output with format()
# the values should be in order to properly format the string

print("Hi {}, how are you doing? are you {} now?".format(name, age))
print("Hi {}, how are you doing? are you {} now?".format(age, name))

print("\n\n")
# format() with named arguments
print("Hi {n}, how are you doing? are you {a} now?".format(n=name, a=age))
print("Hi {n}, how are you doing? are you {a} now?".format(a=age, n=name))


print("\n\n")
# f-strings
formatted_string = f"Hi {name}, how are you doing? are you {age} now?"
print(formatted_string)
# %%
