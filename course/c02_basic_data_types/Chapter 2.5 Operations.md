- **created by**: Sudip Ghimire
- **URL**: [https://www.sudipghimire.com.np](https://www.sudipghimire.com.np)
- **GitHub**: [https://github.com/ghimiresdp](https://github.com/ghimiresdp)

[go to course contents](https://github.com/ghimiresdp/python-level1/)
-----------------------

# Chapter 2.5. Basic Operations

**Table of Contents**

- [Chapter 2.5. Basic Operations](#chapter-25-basic-operations)
    - [arithmetic operations](#arithmetic-operations)
        - [Addition](#addition)
        - [Subtraction](#subtraction)
        - [Multiplication](#multiplication)
        - [Division](#division)
        - [Modulus](#modulus)
        - [Exponentiation](#exponentiation)
        - [Integer Division](#integer-division)
    - [Relational Operations](#relational-operations)
        - [equals (`==`)](#equals-)
        - [not equals (`!=`)](#not-equals-)
        - [less than (`<`)](#less-than-)
        - [less than or equals (`<=`)](#less-than-or-equals-)
        - [greater than (`>`)](#greater-than-)
        - [greater than or equals (`>=`)](#greater-than-or-equals-)
    - [logical operations](#logical-operations)
    - [identity operations](#identity-operations)
    - [membership operations](#membership-operations)
    - [bitwise operations](#bitwise-operations)
    - [assignment operations](#assignment-operations)

## arithmetic operations

Arithmetic operations includes the basic arithmetic operations to different data types. The following are the basic
arithmetic operations

### Addition

**Syntax**: `a + b`

```python
a1 = 5 + 6  # integer and integer
a2 = 5.5 + 2.3  # float and float
a3 = 4.7 + 2  # integer and float
a4 = "Hello " + "world"  # string and string
a5 = (5 + 4j) + (6 + 5j)  # complex and complex
```

### Subtraction

**Syntax**: `a - b`

```python
b1 = 5 - 6  # integer and integer
b2 = 5.5 - 2.3  # float and float
b3 = 4.7 - 2  # integer and float
# b4 = "Hello " - "world"  # string subtraction not supported
b5 = (5 + 4j) - (6 + 5j)  # complex and complex
```

### Multiplication

**Syntax**: `a * b`

```python
c1 = 5 * 6  # integer and integer
c2 = 5.5 * 2.3  # float and float
c3 = 4.7 * 2  # integer and float
c4 = "Hello " * 5  # string and int
c5 = (5 + 4j) * (6 + 5j)  # complex and complex
```

### Division

**Syntax**: `a / b`

```python
d1 = 5 / 6  # integer and integer
d2 = 5.5 / 2.3  # float and float
d3 = 4.7 / 2  # integer and float
d4 = (5 + 4j) / (6 + 5j)  # complex and complex
```

### Modulus

**Syntax**: `a % b`

```python
e1 = 55 % 4  # integer and integer
e2 = 5.5 % 2.3  # float and float
e3 = 4.7 % 2  # integer and float
```

### Exponentiation

**Syntax**: a ** b`

```python
f1 = 5 ** 4  # integer and integer
f2 = 5.5 ** 2.3  # float and float
f3 = 4.7 ** 2  # integer and float
```

### Integer Division

**Syntax**: a // b`

```python
print(5 // 2)
g1 = 45 // 2
g2 = 45.8 // 5.1  # 8.0   # integer equivalent of float

```

## Relational Operations

Relational operations or comparison operations compare 2 values and returns either `True` or `False`. When
comparing `less than` or `greater than` in strings or sequences, it compares the ASCII value using lexicographical
ordering.

### equals (`==`)

```python
print(5 == 6)  # False
print(4 + 1 == 6 - 1)  # True
print('John' == 'John')  # True
```

### not equals (`!=`)

```python
print(5 != 6)  # True
print(4 + 1 != 6 - 1)  # False
print('John' != 'John')  # False

```

### less than (`<`)

```python
print(4 < 5)  # True
print(4 < 4)  # False
print(5 < 4)  # False
print('Jane' < 'John')  # True

```

### less than or equals (`<=`)

```python
print(4 <= 5)  # True
print(4 <= 4)  # True
print(5 <= 4)  # False
print([1, 2, 3] <= [1, 3, 2])  # True

```

### greater than (`>`)

```python
print(4 > 5)  # False
print(4 > 4)  # False
print(5 > 4)  # True
print('Jane' > 'John')  # False
print([1, 2, 3] > [1, 3, 2])  # False

```

### greater than or equals (`>=`)

```python
print(4 >= 5)  # False
print(4 >= 4)  # True
print(5 >= 4)  # True
print('A' >= 'B')  # False
```

## logical operations

## identity operations

## membership operations

## bitwise operations

## assignment operations
