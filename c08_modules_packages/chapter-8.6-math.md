# Chapter 8.6. The `math` Module

**Table of Contents**:

- [Chapter 8.6. The `math` Module](#chapter-86-the-math-module)
  - [Introduction to `math` module](#introduction-to-math-module)
  - [Approximation functions in `math` module](#approximation-functions-in-math-module)
    - [`round` function](#round-function)
    - [`floor` function](#floor-function)
    - [`ceil` function](#ceil-function)
    - [`trunc` function](#trunc-function)
  - [Trigonometry](#trigonometry)
    - [The `math.dist()` function](#the-mathdist-function)
    - [Angular Conversion](#angular-conversion)
  - [Powers and Exponents](#powers-and-exponents)

## Introduction to `math` module

source: <https://docs.python.org/3/library/math.html>

The `math` module provides access to the mathematical functions defined by the C
standard. The module offers various functions such as ceiling, floor values,
permutations combinations, factorials, GCD (HCF), LCM, etc.

## Approximation functions in `math` module

The `math` module provides `floor`, `ceil`, and `trunc` functions to perform
various mathematical approximations.

### `round` function

Rounding is the process of replacing a precise number by another number of
approximately the same value but having fewer digits. example `9.99` can be
approximated to `10` by rounding the decimal digits.

The `round` function does not require `math` module however other functions
related to rounding is available in the module so this function is included in
this module.

To perform rounding, we can just call `round()` method and pass the floating
point number to get the rounded integer value.

The `round()` function takes 1 required argument and 1 optional argument as
follows:

1. `number`: the number that needs to be rounded
2. `ndigits`: the number of decimal digits after which the number is rounded.
   passing `ndigits` will return the floating point value instead of `int`.

```python
x = round(5.85) # 6 (rounded up)

y = round(5.35) # 5 (rounded down)

z = round(4.56678, 3)    # 4.567 (rounded up in the third decimal)

```

### `floor` function

The `floor()` function returns the largest integer that is less than or equal to
the provided number. The `floor()` function takes only one argument and returns
the integer value.

```python
import math

x = math.floor(5.56) # 5
x = math.floor(-5.56) # -6
y = math.floor(5.0)  # 5
```

### `ceil` function

The `ceil()` function returns the smallest integer that is just larger than or
equal to the provided number. The `ceil()` function takes only one argument and
returns the integer value.

```python
import math

x = math.ceil(5.56) # 6
x = math.ceil(-5.56) # -5
y = math.ceil(5.0)  # 5
```

### `trunc` function

The `trunc()` function drops the fractional part of the floating point number.
If the number is negative, it performs `ceil()` function and if the number is
positive, it performs `floor()` function.

```python
import math

x = math.trunc(5.678)   # 5
x = math.trunc(-5.678)  # -5

```

## Trigonometry

source: <https://docs.python.org/3/library/math.html#trigonometric-functions>

The `math` module provides different functions to perform trigonometric
measurements. the `math` function takes angles in radians but not in degrees.

The conversion of radians can be calculated using the formula:

- $1\pi radians = 180\degree$
- $1/2\pi^c = 90\degree$

Some of the trigonometric functions that are available in python `math` module
are as follows:

- `math.sin()`, `math.cos()`, `math.tan()`
- `math.asin()`, `math.acos()`, `math.atan()`

```python
# 0.5pi = 90 degrees
math.sin(0.5*math.pi)   # 1.0
math.cos(0.5*math.pi)   # 6.123233995736766e-17 ≈ 0.00000000000000006123

# finding out the inverse (arc) of a number
math.asin(0.5)  # 0.5235987755982988 ≈ 30°
```

### The `math.dist()` function

The `math.dist()` function finds out the eucledian distance between 2 points.
the distance between 2 points is found out using the formula:

- $distance =\sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 }$

```py
a = (0, 0)
b = (3, 4)
print(math.dist(a, b))  # 5.0
```

### Angular Conversion

The python `math` module also offers the conversion between `degrees` and
`radians`.

```py
print(math.radians(180))      #  3.141592653589793
print(math.degrees(math.pi))  #  180.0
```

## Powers and Exponents

The python `math` module also provides powerful methods to find different
exponential and logarithmic functions.

some of the methods are as follows:

- `math.crbt(x)`: Returns the cube root of `x`.
- `math.sqrt(x)`: Returns the square root of `x`.
- `math.pow(x, y)`: Returns the value of $x^y$.
- `math.exp(x)`: Returns $e^x$ where $e=2.178281..$
- `math.expm1(x)`: Returns inverse of x.
- etc.

Example:

```py
print(math.sqrt(16))  # 4.0
print(math.exp(5))    # 148.4131591025766
```
