"""
© https://sudipghimire.com.np


Write a program to create an empty list named `my_list` and

a. add numbers 5 and 9 to the list using `append()` method

b. ask the user to input any number in the console and add the number to the list.
    - you can use int() to change the type from string to integer if you want.

c. create another list `more_items` with 3 items on it and extend the list `my_list`
    using `extend` method.

d. now find the length of the list and print the length of list describing it in a sentence.
    - you can use string formatting for better outputs.

e. now remove the second item using `pop()` method and see if the item exists in the list
    - you can print the list before and after using the `pop()` method.
"""

my_list = []

# a
my_list.append(5)
my_list.append(9)
print(f"The list is {my_list}")


# b
num = input("Enter a number to append: ")
my_list.append(int(num))
print(f"The list after appending {num} is {my_list}")
# c

more_items = [3, 4, 5]
my_list.extend(more_items)
print(f"The list after extending with {more_items} is {my_list}")

# d
print(f"Length of the list is {my_list.__len__()}")

# e
print("List before popping out second item:", my_list)
my_list.pop(1)
print("List after popping out second item:", my_list)
