"""
© https://sudipghimire.com.np

Create two variables first_name, and last_name and print the sentence in the format below:
suppose first_name is John and last_name is Doe
"My name is John Doe"

1. use + operator to concatenate strings
2. use format() method to achieve the same result
3. use f-strings to achieve the same result
4. use %s formatting method to achieve the same result

"""
# answer

first_name = "John"
last_name = "Doe"

# 1
full_name = "My Name is " + first_name + " " + last_name
print(full_name)

# 2

full_name_formatted = "My Name is {} {}".format(first_name, last_name)

print(full_name_formatted)

# 3
full_name_fstring = f"My Name is {first_name} {last_name}"
print(full_name_fstring)

# 4
full_name_s = "My Name is %s %s" % (first_name, last_name)
print(full_name_s)
