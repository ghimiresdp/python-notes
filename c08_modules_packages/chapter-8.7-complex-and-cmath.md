# Chapter 8.7. Complex numbers and `cmath` module

**Table of Contents**:

- [Chapter 8.7. Complex numbers and `cmath` module](#chapter-87-complex-numbers-and-cmath-module)
  - [A complex number](#a-complex-number)
  - [Absolute value of the imaginary number](#absolute-value-of-the-imaginary-number)
  - [the `cmath` module](#the-cmath-module)
    - [Constants](#constants)
    - [finding out the phase of the complex number](#finding-out-the-phase-of-the-complex-number)
    - [finding out log and exponents using cmath module](#finding-out-log-and-exponents-using-cmath-module)

## A complex number

Complex number is a number with combination of real and imaginary part. It is denoted by `a + ib` where `a` is the real part of the number and `b` is the imaginary part. `i` is the representation of imaginary part. In python, we use the format `(a + bj)`.

In python, complex numbers are builtin data type. We can perform complex operations without importing any external libraries but if we want to perform advanced calculations, we can use `cmath` library which comes along with python.

The following code shows an example of a structure of a complex number used in python.

```py
x = 5 + 4j
x = 6 + 1j  # we cannot write "6 + j" as in mathematics
x = 2 + 0j

print(x)    # (5+4j)
print(type(x))  # <class 'complex'>
```

## Absolute value of the imaginary number

We can use inbuilt `abs()` function to find out the absolute value of the imaginary number.

```py
x = 2 + 3j

print(abs(x))
# 3.605551275463989
```

## the `cmath` module

The `cmath` module deals with the complex numbers functions. It is able to perform complex calculations such as finding out the square root, changing the coordinate from rectangular to polar coordinates, etc.

some of the example are as follows:

```py
import cmath

# Converting rectangular coordinates to polar
x = 5 + 4j
print(cmath.polar(x))
# (6.4031242374328485, 0.6747409422235526)


# Converting polar coordinates to rectangular
print(cmath.rect(4, 3))
# (-3.9599699864017817 + 0.5644800322394689j)
```

### Constants

Some constants such as `pi` or `e` are provided with cmath module however constants such as `inf` and `nan` are available in `math` module since python >=3.5

```python
import math
import cmath

print(cmath.pi)
# 3.141592653589793

print(cmath.e)
# 2.718281828459045

print(math.inf)
# inf

print(math.nan)
# nan
```

### finding out the phase of the complex number

```python
import cmath

print(cmath.phase(5 + 4j))
# 0.6747409422235526
```

### finding out log and exponents using cmath module

```python
import cmath

x = 5 + 4j

print(cmath.exp(x))
# (-97.0093146996155 - 112.31944914536253j)

print(cmath.log(x))
# (1.856786033352154 + 0.6747409422235526j)

print(cmath.log10(-50))
# (1.6989700043360185 + 1.3643763538418412j)
 ```
