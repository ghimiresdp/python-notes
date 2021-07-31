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

for lang_type in lang:
    for lng in lang[lang_type]:
        print(f'The {lang_type} programming language is {lng}')

# %% example
x = [[1, 2, 3], [4, 55, 20], [7, 8, 9]]
for a in x:
    for b in a:
        print(b)

# %% for loop with more than one value at once
tuples = ((1, 2, 3), (5, 8, 6), (0, 3, 8))

for (a, b, c) in tuples:
    print(f'the first one is {a},'
          f' and the second one is {b} , and finally {c}')

# %% if we do not need some variables we can ignore them usinge underscore `_`.

for (a, b, _) in tuples:
    print(f'the first is {a} and the second is {b}')

# %% example 2
# print 'Hello World' 10 times
for _ in range(10):
    print("Hello World")

# %%
x = [1, 4, 3, 6, 3, 7, 5, 9, ]

i1 = x.index(6)
i2 = x.index(7)
if i1 < i2:
    x = [*x[:i1], *x[i2 + 1:]]
    # for l in range(i1, i2):
    #     x.pop(l)
print(x)

# %% pattern generation 1
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
for x in range(1, 6):
    for y in range(1, x + 1):
        print(y, end=' ')
    print()

# %% pattern generation 2
"""
1	2	3	4	5
2	4	6	8	10
3	6	9	12	15
4	8	12	16	20
5	10	15	20	25
"""
for x in range(1, 6):
    for y in range(1, 6):
        print(y * x, end='\t')
    print()

# %%
"""
1	2	3	4	5
1	4	9	16	25
1	8	27	64	125
1	16	81	256	625
1	32	243	1024	3125
"""
for x in range(1, 6):
    for y in range(1, 6):
        print(y ** x, end='\t')
    print()

# %% pattern generation 3
"""
1
2	2
3	3	3
4	4	4	4
5	5	5	5	5
"""
# %%
for x in range(1, 6):
    for _ in range(1, x + 1):
        print(x, end='\t')
    print()

# %% pattern generation 4

"""
                1
            1	2	3
        1	2	3	4	5
    1	2	3	4	5	6	7
1	2	3	4	5	6	7	8	9


# pattern 1 -> spaces
1. [				] -> 4 spaces (\t)
2. [			] -> 3 spaces
3. [		] -> 2 spaces
4. [	] -> 1 space
5. [] -> no spaces


# pattern 2 -> numbers

1. [1]
2. [1	2	3]
3. [1	2	3	4	5]
4. [1	2	3	4	5	6	7]
5. [1	2	3	4	5	6	7	8	9]

# pattern 3: combine each step of pattern 1 and 2

1.  [				]1
2.  [			]1	2	3
3.  [		]1	2	3	4	5
4.  [	]1	2	3	4	5	6	7
5.  []1	2	3	4	5	6	7	8	9

# The final output:
1. 				    1
2.			    1	2	3
3.		    1	2	3	4	5
4.	    1	2	3	4	5	6	7
5.  1	2	3	4	5	6	7	8	9
"""

# %% the simpler method
for x in range(1, 6):
    print('\t' * (5 - x), end='')
    for y in range(1, (x * 2)):
        print(y, end='\t')
    print()

# %% the other method
for x in [1, 3, 5, 7, 9]:

    # pattern 1 (printing the spaces)
    print('\t' * ((9 - x) // 2), end='')

    # pattern 2 looping through the numbers
    for y in range(1, x + 1):
        print(y, end='\t')

    # the next line
    print()

# %% with console feedback
for x in [1, 3, 5, 7, 9]:
    spaces = ('\t' * ((9 - x) // 2))
    print(f'[{spaces}]', end='')
    for y in range(1, x + 1):
        print(y, end='\t')
    print()
    # print(f'[{spaces}]')

# %% advanced method
for x in [r for r in range(1, 10) if r % 2 != 0]:
    print('\t' * ((9 - x) // 2), end='')
    for y in range(1, x + 1):
        print(y, end='\t')
    print()
