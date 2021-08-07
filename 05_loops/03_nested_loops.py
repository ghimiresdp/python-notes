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
1	2
1	2	3
1	2	3	4
1	2	3	4	5
"""

for x in range(1, 6):
    for y in range(1, x + 1):
        print(y, end='\t')
    print()

# %%

# line 1
for x in range(1, 2):
    print(x, end='\t')
print()

# line 2
for x in range(1, 3):
    print(x, end='\t')
print()

# line 3
for x in range(1, 4):
    print(x, end='\t')
print()

# line 4
for x in range(1, 5):
    print(x, end='\t')
print()

# line 5
for x in range(1, 6):
    print(x, end='\t')
print()

# now we have to see what is changing
# here values in range are changing i.e. [2,3,4,5,6]
# we have to create a range from 2 -> 6
# the function is range(2,7)

# the solution would be -> for x in range(2,7)

# %%

for x in range(2, 7):
    for y in range(1, x):
        print(y, end='\t')
    print()

# %% advanced usage
for x in range(1, 6):
    print('\t'.join([str(y) for y in range(1, x + 1)]))

# %% more advanced usage
print('\n'.join(['\t'.join([str(y) for y in range(1, x + 1)]) for x in range(1, 6)]))

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

# %% advanced usage
for x in range(1, 6):
    print('\t'.join([str(y * x) for y in range(1, 6)]))

# %% more advanced usage
print('\n'.join(['\t'.join([str(y * x) for y in range(1, 6)]) for x in range(1, 6)]))

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

# %% advanced usage
for x in range(1, 6):
    print('\t'.join([str(y ** x) for y in range(1, 6)]))
# %% more advanced usage
print('\n'.join(['\t'.join([str(y ** x) for y in range(1, 6)]) for x in range(1, 6)]))

# %% pattern generation 3
"""
1
2	2
3	3	3
4	4	4	4
5	5	5	5	5

variations:
1.  [1, 2, 3, 4, 5] or [2, 3, 4, 5, 6]

"""
for x in range(1, 6):
    for y in range(1, x + 1):
        print(x, end='\t')
    print()
# %%
# simpler method
for x in range(1, 6):
    for _ in range(1, x + 1):
        print(x, end='\t')
    print()

# %% advanced usage
for x in range(1, 6):
    print('\t'.join([str(x) for x in range(1, x + 1)]))

# %% more advanced usage
print('\n'.join(['\t'.join([str(x) for y in range(1, x + 1)]) for x in range(1, 6)]))

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
# %%

# ________________ line 1
print('\t' * 4, end='\t')
for y in range(1, 2):
    print(y, end='\t')
print()

# ________________ line 2
print('\t' * 3, end='\t')
for y in range(1, 4):
    print(y, end='\t')
print()

# ________________ line 3
print('\t' * 2, end='\t')
for y in range(1, 6):
    print(y, end='\t')
print()

# ________________ line 4
print('\t' * 1, end='\t')
for y in range(1, 8):
    print(y, end='\t')
print()

# ________________ line 5
print('\t' * 0, end='\t')
for y in range(1, 10):
    print(y, end='\t')
print()

# the next step is finding out the changes (variables)
# 1. no. of spaces is varying [4, 3, 2, 1, 0]
# 2. end of range is varying [2, 4, 6, 8, 10]
# next we generate pattern

# [1, 2, 3, 4, 5]

# [4, 3, 2, 1, 0]
# [2, 4, 6, 8, 10]


# %%
for x in range(1, 6):
    print('\t' * (5 - x), end='\t')
    for y in range(1, 2 * x):
        print(y, end='\t')
    print()

# %%


# the simpler method
for x in range(1, 6):
    print('\t' * (5 - x), end='')
    for y in range(1, (x * 2)):
        print(y, end='\t')
    print()

# %% advanced usage
for x in range(1, 6):
    print('\t' * (5 - x), end='')
    print('\t'.join([str(y) for y in range(1, (x * 2))]))

# %% more advanced usage
print('\n'.join(['\t' * (5 - x) + '\t'.join([str(y) for y in range(1, (x * 2))]) for x in range(1, 6)]))

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

# %% the other method [advanced]
for x in [r for r in range(1, 10) if r % 2 != 0]:
    print('\t' * ((9 - x) // 2), end='')
    for y in range(1, x + 1):
        print(y, end='\t')
    print()
