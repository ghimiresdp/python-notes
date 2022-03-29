"""
© https://sudipghimire.com.np


Try creating a multi-dimensional list or nested list `multi` of different numbers.
    eg: [[12,52,37],[46,51,16],[17,82,39]]

a. access the number 51 from the list.
b. access the number 82 using the negative indices.
c. append another list [40, 61, 10] inside the list `multi`.
    the final list should be: [[12,52,37],[46,51,16],[17,82,39],[40, 61, 10]]
d. use foreach in the list `multi` to print each list item to the console.
    - Bonus: try using nested foreach to access each item inside of the inner list
e. finally clear the list `multi` using the `clear()` method and verify if the list is empty or not
"""

multi = [[12, 52, 37], [46, 51, 16], [17, 82, 39]]

# a
print(multi[1][1])

# b
print(multi[-1][-2])

# c
multi.append([40, 61, 10])
print(multi)

# d
for item in multi:
    print(f'the item is: {item}')
    for inner_item in item:
        print("the inner item is: ", inner_item)

# e
multi.clear()
print("the list after clearing is: ", multi)
