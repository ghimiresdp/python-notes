# Chapter 5.3: Pattern Generation

**Table of Contents**:

- [Chapter 5.3: Pattern Generation](#chapter-53-pattern-generation)
  - [Pattern 1](#pattern-1)
  - [Pattern 2](#pattern-2)
  - [Pattern 3](#pattern-3)
  - [Pattern 4](#pattern-4)

## Pattern 1

```
A A A A A
A A A A A
A A A A A
A A A A A
A A A A A
```

**Solution:**

```python
for x in range(5):
    for y in range(5):
        print('A', end=' ')
    print()
```

## Pattern 2

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

**Solution:**

```python
for row in range(1, 6):
    for col in range(1, row + 1):
        print(col, end='  ')
    print()
```

## Pattern 3

```
1
2  2
3  3  3
4  4  4  4
5  5  5  5  5
```

**Solution:**

```python
for row in range(1, 6):
    for col in range(row):
        print(row, end='  ')
    print()
```

## Pattern 4

```
            1
         2  1
      3  2  1
   4  3  2  1
5  4  3  2  1
```

**Explanation:**

- Row 1:  No. of cols = 1, spaces = 4, value = `1`
- Row 2:  No. of cols = 2, spaces = 3, value = `Row ... 1` = `2 1`
- Row 3:  No. of cols = 3, spaces = 2, value = `Row ... 1` = `3 2 1`
- ...

**Solution:**

```python
for row in range(1, 6):
    # printing out spaces
    print('   ' * (5 - row), end='')
    # printing out patterns
    for col in range(row, 0, -1):
        print(col, end='  ')
    print()
```
