"""
Q0303 solutions

https://sudipghimire.com.np
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
