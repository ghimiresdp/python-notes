"""
Q0302 solutions

https://sudipghimire.com.np
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
