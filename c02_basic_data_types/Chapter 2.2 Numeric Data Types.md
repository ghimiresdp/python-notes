# Chapter 2.2: Numeric Data types

**Table of Contents**:

- [Chapter 2.2: Numeric Data types](#chapter-22-numeric-data-types)
  - [1. Integers `int`](#1-integers-int)
  - [2. Floating Point Numbers `float`](#2-floating-point-numbers-float)
  - [3. Complex data types `complex`](#3-complex-data-types-complex)
  - [4. Boolean Data types `bool`](#4-boolean-data-types-bool)

## 1. Integers `int`

Integers are those data types that contains either positive or negative numbers without any decimal points.

```python
num1 = 5        # decimal number

# We can also assign binary, octal, or hexadecimal numbers

num2 = 0x4a     # hexadecimal number
num3 = 0b101    # binary number
num4 = 0o447    # Octal number

num5: int = -5   # optional type hinting
```

## 2. Floating Point Numbers `float`

Floating point numbers are those data types that can contain decimal values.

```python
num1 = 5.5
num2 = -5.5
num3: float = 5.5   # optional type hinting
```

## 3. Complex data types `complex`

Unlike other programming languages, python comes with built in complex data types. we store the data in format:

 `real` + `imaginary` `j`

```python
comp1 = 5 + 4j
comp2 = -5j
comp3: complex = 8 - 5j     # optional type hinting
```

## 4. Boolean Data types `bool`

We can count Boolean data types as both numeric and logical data types since `True` represents `1` and `False` represents `0`. In python we have keywords assigned for Boolean data types.

```python
engaged = True
married = False

alive: bool = True      # optional type hinting
```
