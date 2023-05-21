# https://sudipghimire.com.np
# %%
"""
Lists

1. Lists can store multiple items in a single variable
2. Lists are created using Square brackets []
3. Items in list are ordered
4. The first item of list has index of 0
5. List with n number of items has last index of (n-1)
6. Lists are different than Arrays in other programming languages.
    - lists can have more than one type of data
    - lists are mutable
    - lists do not need data to be unique
"""
# %%
list_one = [1, 2, 3, 4, 5]

# creating a list
numbers = [18, 24, 56, 21, 44, 27, 99, 100, 64, 44]
animals = ['cat', 'dog', 'tiger']
random_lists = [1, 'John', 'Moon', True, 45.62]
# %%
# in case of a list, new line do not terminate the statement until it finds the closing brackets
# indentation doesnot matter inside lists, but is recommended.
animals = [
    "Cat",
    "Dog",
    'Tiger',
]
print(animals)
# %%
# accessing an item of a list
print(numbers[0])
print(animals[2])

# if we try to access the item with the index larger than the length of the list, it throws an exception
# list index out of range
# animals[10]  -> results in list index out of range exception
# %%
# accessing an item of a list with reverse index
print(animals[-1])
print(random_lists[-3])
# %%
# accessing a range of items from a list with `[<a>:<b>]`
# a -> start of the range (inclusive)
# b -> end of the range (exclusive)
# can also be the negative index

print(random_lists[2:4])
print(random_lists[-3:-1])
# %%
# a or b can be empty
# in this case, it counts from the index 2 upto the end of the list
print(random_lists[2:])
# n[0:4] is equivalent to n[:4])
# in this case, it counts from the beginning upto 4th index of the list
print(random_lists[:4])
# %%
# length of a list
print(animals.__len__())
print(len(animals))

# %%
# Updating a value of a list
animals[0] = 'Elephant'
# %%
# updating a value of a range of a list
numbers[2:4] = [16, 18]
# %%
# adding an item to the list
animals.append("Monkey")
# %%
# adding an item to the specific index
# the first parameter would be the index
# the second parameter would be the value
animals.insert(2, "Lion")
# %%
# adding multiple items to the list (Extending)
more_animals = ['Chimpanzee', 'Fox', 'Deer']
animals.extend(more_animals)

# or we can directly add animals by passing the list as the parameter
animals.extend(['Giraffe', 'Zebra', 'Buffalo'])

# removing an item from the list
animals.remove("Buffalo")
# if it can't find the item to remove from the list, then it throws an exception

animals.remove("ABCDEF")  # gives an error

# removing the last item of the list
animals.pop()

# removing an item of the list with specific index
animals.pop(3)
# if it can't find the index of the item it gives "index out of range" exception


# removing all items of a list
# we can achieve this with two different method
# 1. assign list to empty list []
# 2. list.clear()

animals.clear()
animals = []  # it does the same

# other List methods
"""
copy()          -> copies the value of the list to another one
reverse()       -> reverses the list
sort()          -> sorts the list in an ascending order
index(value)    -> returns the index of the first element with the given value
count(value)    -> returns the count of elements with the given value

"""
animals_2 = animals.copy()
animals.sort()
animals.reverse()
animals.index('cat')
animals.count('cat')

# nested lists
x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# we can visualize it in the matrix form also

x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

three_dim = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
]

# accessing an item of the nested list
print(x[0])     # [1,2,3]

print(x[0][0])  # [1]

# foreach in the list
for animal in animals:
    print(animal)


# for practice
# method 1

[[[(x+a+b) for b in range(3)] for a in range(3)] for x in range(5)]

# method 2
arr = []
for x in range(3):
    tmp = []
    for y in range(3):
        tmp_2 = []
        for z in range(3):
            tmp_2.append(x+y+z)
        tmp.append(tmp_2)
    arr.append(tmp)
