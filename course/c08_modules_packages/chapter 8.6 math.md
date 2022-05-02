- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp

# 8.6. The `math` Module
source: https://docs.python.org/3/library/math.html

The `math` module provides access to the mathematical functions defined by the C standard. The module offers various functions such as ceiling, floor values, permutations combinations, factorials, GCD (HCF), LCM, etc.

**Table of Contents**
- [8.6. The `math` Module](#86-the-math-module)
  - [Approximation functions in `math` module](#approximation-functions-in-math-module)
    - [`round` function](#round-function)
    - [`floor` function](#floor-function)
    - [`ceil` function](#ceil-function)
    - [`trunc` function](#trunc-function)
  - [Trigonometry](#trigonometry)
  - [Powers and Exponents](#powers-and-exponents)

## Approximation functions in `math` module
The `math` module provides `floor`, `ceil`, and `trunc` functions to perform various mathematical approximations.

### `round` function
Rounding is the process of replacing a precise number by another number of approximately the same value but having fewer digits. example `9.99` can be approximated to `10` by rounding the decimal digits.


The `round` function does not require `math` module however other functions related to rounding is available in the module so this function is included in this module.

To perform rounding, we can just call `round()` method and pass the floating point number to get the rounded integer value.

The `round()` function takes 1 required argument and 1 optional argument as follows:
1. `number`: the number that needs to be rounded
2. `ndigits`: the number of decimal digits after which the number is rounded. passing `ndigits` will return the floating point value instead of `int`.

```python
x = round(5.85) # 6 (rounded up)

y = round(5.35) # 5 (rounded down)

z = round(4.56678, 3)    # 4.567 (rounded up in the third decimal)

```

### `floor` function

The `floor()` function returns the largest integer that is less than or equal to the provided number. The `floor()` function takes only one argument and returns the integer value.

```python
import math

x = math.floor(5.56) # 5
x = math.floor(-5.56) # -6
y = math.floor(5.0)  # 5
```

### `ceil` function

The `ceil()` function returns the smallest integer that is just larger than or equal to the provided number. The `ceil()` function takes only one argument and returns the integer value.

```python
import math

x = math.ceil(5.56) # 6
x = math.ceil(-5.56) # -5
y = math.ceil(5.0)  # 5
```

### `trunc` function

The `trunc()` function drops the fractional part of the floating point number. If the number is negative, it performs `ceil()` function and if the number is positive, it performs `floor()` function.

```python
import math

x = math.trunc(5.678)   # 5
x = math.trunc(-5.678)  # -5

```

## Trigonometry
source: https://docs.python.org/3/library/math.html#trigonometric-functions

The `math` module provides different functions to perform trigonometric measurements.

## Powers and Exponents


