"""
© https://sudipghimire.com.np


Write a program to add 5 different wild animals to a list named `wild`.
    - tiger, lion, deer, bear, zebra

a. sort them in ascending using the `sort()` method.
b. reverse the list using the `reverse()` method.
c. now add 3 more animals to the list `wild`.  ['leopard', 'elephant', 'rhino']
d. find the position of `leopard` using the `index()` method and remove  it using `the pop()` method.
    - pop should have the index value returned using the `index()` method.
    - do not hard-code the position of leopard by manually counting it from the list.
    - check whether the leopard is removed from the list or not by `index()` method again.
        if the value error occurs, you have successfully removed it from the list.
        otherwise, try to do it again.
    - you can then comment the line that gives exception to continue to the next question.
e. Now add `leopard` agin in the index 2 using `insert()` method.
f. Again, remove `rhino` from the list using remove() method.

note: you can print the values of list after each successful operations to see what is being changed.
"""

wild = ['tiger', 'lion', 'deer', 'bear', 'zebra']

# a

wild.sort()
print("List after sorting: ", wild)


# b
wild.reverse()
print("List after Reversing: ", wild)

# c
wild.extend(['leopard', 'elephant', 'rhino'])
print("List after extending more animals: ", wild)

# d
print("the index of leopard is: ", wild.index('leopard'))

index = wild.index('leopard')
wild.pop(index)
print("List after removing leopard: ", wild)

# index = wild.index('leopard')     #this gives error since 'leopard' has already been removed from the list

# e
wild.insert(2, "leopard")
print("List after re-inserting leopard: ", wild)
# f
wild.remove('rhino')
print("List after removing rhino: ", wild)
