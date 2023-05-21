"""
Q0203 solutions

https://sudipghimire.com.np
"""

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
