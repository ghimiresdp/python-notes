# © https://sudipghimire.com.np
# %% [markdown]
"""
Nested Loops
- Nested loops are loops inside loops
"""
# %% nested loop basic syntax
lang = {
    'low level': ['Machine Level', 'Assembly'],
    'high level': ['C++', 'Java', 'Python']
}

for name in lang:
    for lng in lang[name]:
        print(f'The {name} programming language is {lng}')

# %% pattern generation 1

for x in range(1, 6):
    for y in range(1, x + 1):
        print(y, end=' ')
    print()

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""

# %% pattern generation 2

for x in range(1, 6):
    for y in range(1, 6):
        print(y * x, end='\t')
    print()

"""
1	2	3	4	5
2	4	6	8	10
3	6	9	12	15
4	8	12	16	20
5	10	15	20	25
"""

# %% pattern generation 3

for x in range(6):
    for y in range(1, x + 1):
        print(x, end='\t')
    print()

"""
1
2	2
3	3	3
4	4	4	4
5	5	5	5	5
"""


# %% pattern generation 4

for x in [1, 3, 5, 7, 9]:
    print('\t' * ((9 - x) // 2), end='')
    for y in range(1, x + 1):
        print(y, end='\t')
    print()

"""
                1
            1	2	3
        1	2	3	4	5
    1	2	3	4	5	6	7
1	2	3	4	5	6	7	8	9
"""
