# https://sudipghimire.com.np
"""
Strings in Python

- single quotes
- double quotes
- escape characters
- quotation inside quotes
- concatenation
- length of the string
- capitalization
- isdecimal

Formatting strings:
- %s
- `format()` function
- f-strings

"""

# We can use Single quote for strings
name = 'John'

# We can use double quotes for strings
name = "John"

# We can use single quotes inside double or vice versa
x = "I am at John's"
x = 'He said, "John is a cool guy!"'

# If we want to have special characters or
# We want single inside single quotes or double quotes inside double quotes, we have to use escape characters

# We can achieve escape characters by using backslash `\` before the character.
x = 'I am at John\'s'  # this will output :  I am at John's

# some of the examples of escape characters and their use cases are as follows:
"""
\t => tabs
\n => new lines
\" => double quotes
\' => single quotes
\\ => backslash
\a => ascii bell
\b => backspace
\r => carriage return
\v => vertical tab
for more detail about escape characters, please see https://docs.python.org
"""

two_lines = "This is the first line.\nThis is the second line."

paragraph = "Microsoft and our third-party\n vendors use cookies to store and access information such as unique IDs to deliver, maintain and improve our\n services and ads. If you agree, MSN and Microsoft Bing will personalize the content and ads that you see. You can select \"I Accept\" to consent to these uses or click on \"Manage preferences\" to review your options  You can change your selection under \"Manage\n Preferences\" at the bottom of this page.\n\n\n"

print(paragraph)

hobbies = "\n\n1.\tsinging\n2.\tdancing\n3.\tcoding"
print(hobbies)

# Concatenation
# it is the process of adding or joining 2 strings together

first_name = "Mohammad"
last_name = "Ibrahim"

full_name = "Mohammad" + "Ibrahim"  # MohammadIbrahim

print("My name is " + full_name)  # My name is MohammadIbrahim

full_name = "My name is " + first_name + " " + last_name  # My name is Mohammad Ibrahim

# length of the string
"""
we can get the length of string with `__len__()` method

the method gives the length of string including all the white spaces and special characters
"""

length = paragraph.__len__()

print("the length of the paragraph is: " + str(length))

print("Mohammad".__len__())  # 8

print("John Doe".__len__())  # 8

# capitalization, Upper Case, and Lower Case

print("john".capitalize())  # John

print("john".upper())  # JOHN
print("JOHN".lower())  # john

# isdecimal()
value = "10"
print(value.isdecimal())  # True
print("123stu".isdecimal())  # False
