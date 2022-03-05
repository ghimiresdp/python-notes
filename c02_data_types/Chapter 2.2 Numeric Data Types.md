- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

# Chapter 2: Python Variables and Data Types

## Basic Data Types

Data Types are the variables that we use to reserve some space in memory. Data types define how the data is stored and how it behaves in different situations. For example `1` + `1` equals `2`, but `A` + `B` can not be `C`. This kind of properties are defined by data types.

Unlike other programming languages, we do not declare data type explicitly. Since python 3.6 Optional type-hinting is introduced in python.

## Numeric Data types

There are 3 basic data types in python which are as follows

### 1. Integers `int`

Integers are those data types that contains either positive or negative numbers without any decimal points.

```python
num1 = 5        # decimal number

# We can also assign binary, octal, or hexadecimal numbers

num2 = 0x4a     # hexadecimal number
num3 = 0b101    # binary number
num4 = 0o447    # Octal number

num5: int = -5   # optional type hinting
```

### 2. Floating Point Numbers `float`

Floating point numbers are those data types that can contain decimal values.

```python
num1 = 5.5
num2 = -5.5
num3: float = 5.5   # optional type hinting
```

### 3. Complex data types `complex

Unlike other programming languages, python comes with built in complex data types. we store the data in format:

 `real` + `imaginary` `j`

```python
comp1 = 5 + 4j
comp2 = -5j
comp3: complex = 8 - 5j     # optional type hinting
```

### Boolean Data types `bool`

We can count Boolean data types as both numeric and logical data types since `True` represents `1` and `False` represents `0`. In python we have keywords assigned for Boolean data types.

```python
engaged = True
married = False

alive: bool = True      # optional type hinting
```
