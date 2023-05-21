from itertools import groupby

"""
`groupby()` function
"""
# example 1
animals = ['Bear', 'Donkey', 'Cat', 'Dog', 'Camel', 'Elephant']
animals = sorted(animals)
values = groupby(animals, lambda x: x[0])
grouped = {k: list(v) for k, v in values}
print(grouped)

# {'B': ['Bear'], 'C': ['Camel', 'Cat'], 'D': ['Dog', 'Donkey'], 'E': ['Elephant']}

# Example 2
coordinates = ((1, 2), (2, 3), (3, 4), (1, 3), (2, 4), (1, 4))
f = lambda f: f[0]

grouped = groupby(sorted(coordinates, key=f), f)

print({k: list(v) for k,v in grouped})
# {1: [(1, 2), (1, 3), (1, 4)], 2: [(2, 3), (2, 4)], 3: [(3, 4)]}
