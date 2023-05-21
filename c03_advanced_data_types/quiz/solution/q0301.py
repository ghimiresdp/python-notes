"""
Q0301 solutions

https://sudipghimire.com.np
"""

my_list = []

# 1
my_list.append(5)
my_list.append(9)
print(f"The list is {my_list}")


# 2
num = input("Enter a number to append: ")
my_list.append(int(num))
print(f"The list after appending {num} is {my_list}")

# 3
more_items = [3, 4, 5]
my_list.extend(more_items)
print(f"The list after extending with {more_items} is {my_list}")

# 4
print(f"Length of the list is {len(my_list)}")  # using len() function
print(f"Length of the list is {my_list.__len__()}") # using class method

# 5
print("List before popping out second item:", my_list)
my_list.pop(1)
print("List after popping out second item:", my_list)
