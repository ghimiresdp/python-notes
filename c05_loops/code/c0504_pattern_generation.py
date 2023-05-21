# Nested loop for pattern Generation
"""
A A A A A
A A A A A
A A A A A
A A A A A
A A A A A
"""

for i in range(5):
    for j in range(5):
        print('A', end='  ')
    print()

"""
1
1	2
1	2	3
1	2	3	4
1	2	3	4	5
"""
"""
Row 1:  No. of cols = 1
Row 2:  No. of cols = 2
Row 3:  No. of cols = 3
...
"""
for row in range(1, 6):
    for col in range(1, row + 1):
        print(col, end='  ')
    print()


for row in range(1, 6):
    for col in range(1, row + 1):
        print(col * 3, end='  ')
    print()


"""
1
2  2
3  3  3
4  4  4  4
5  5  5  5  5
"""
"""
Row 1:  No. of cols = 1, values = 1
Row 2:  No. of cols = 2, values = 2
Row 3:  No. of cols = 3, values = 3
...
"""
for row in range(1, 6):
    for col in range(1, row + 1):
        print(row, end='  ')
    print()


"""
            1
         2  1
      3  2  1
   4  3  2  1
5  4  3  2  1

Row 1:  No. of cols = 1, spaces = 4, value = 1
Row 2:  No. of cols = 2, spaces = 3, value = Row -> 1
Row 3:  No. of cols = 3, spaces = 2

"""
for row in range(1, 6):
    # printing out spaces
    print('   ' * (5 - row), end='')
    # printing out patterns
    for col in range(row, 0, -1):
        print(col, end='  ')
    print()
