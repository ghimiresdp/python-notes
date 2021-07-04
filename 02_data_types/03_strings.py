"""
© https://sudipghimire.com.np

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
'this is a string'
"this is a string"

# single quotes

name_k = 'kusum'
print(name_k)

# double quotes
name_r = "Rosan"
print(name_r)

# single quotes inside double quotes
cow = "Cow is an animal. cow's tail is so long."


# escape characters
cow = 'Cow is an animal. cow\'s tail is so long.'

# some of the examples of escape characters
"""
\t -> tabs
\n -> new lines
\" -> double quotes
\' -> single quotes
"""

two_lines = "This is the first line.\nThis is\nthe second line."
print(two_lines)

hubby =  "knitting"

hubby  =  "singing" 


paragraph = "Microsoft and our third-party\n vendors use cookies to store and access information such as unique IDs to deliver, maintain and improve our\n services and ads. If you agree, MSN and Microsoft Bing will personalize the content and ads that you see. You can select \"I Accept\" to consent to these uses or click on \"Manage preferences\" to review your options  You can change your selection under \"Manage\n Preferences\" at the bottom of this page.\n\n\n"

print(paragraph)


# please print your 2 hobbies with the same string but in the different lines using escape characters


hobbies = "1. singing 2. knitting 3. singing 4. knitting 5. singing 6. knitting"
print (hobbies)

hobbies = "\n\n1.\tsinging\n2.\tknitting\n3.\tsinging\n4.\tknitting\n5.\tsinging\n6. knitting"
print (hobbies)


# Concatenation
# it is the process of adding 2 strings together

first_name = "Mohammad"
last_name = "Ibrahim"
last_name_2 = "Ali"

name = "Mohammad " + "Ibrahim"

print("My name is " + name)

full_name = "My name is " + first_name + " " + last_name

print("\n\n\n")

print(full_name)
full_name2 = "My name is " + first_name + " " + last_name_2
print(full_name2)


# length of the string

length = paragraph.__len__()

print("the length of the paragraph is " + str(length))

print("\n\n")
print("Mohammad".__len__())
print("\n\n")

print("kusum".__len__())
print("kusum dahal".__len__()) 

# capitalization, Upper Case, and Lower Case

print("kusum".capitalize()) # Kusum

print("mohammad".upper())   # MOHAMMAD
print("ROSHAN".lower()) # roshan

# is decimal

value = "10"
print(value.isdecimal())    # True


value = "234eg"
print(value.isdecimal())    # False



# string formatting 