> - **created by**: Sudip Ghimire
> - **URL**: https://www.sudipghimire.com.np
> - **GitHub**: https://github.com/ghimiresdp
>
> [go to course contents](https://github.com/ghimiresdp/python-notes/)

# Chapter 13.5: The `reduce()` Function

**Table of Contents**

- [Chapter 13.5: The `reduce()` Function](#chapter-135-the-reduce-function)
  - [Introduction to `reduce` function](#introduction-to-reduce-function)

## Introduction to `reduce` function

The `reduce` function performs calculation on all elements by iterating on items
of an iterable. For example, we can find out the product of all numbers of a
list. The function `reduce` can be imported from `functools` builtin library.

The first parameter of the `reduce` function takes a function as a parameter
that takes exactly 2 arguments. To reduce the iterable it first takes first 2
elements and performs operation. The result of them is then fed to the function
again with another element until the iterable gets exhausted.

```python
from functools import reduce

numbers = [1, 12, 30, 24, 8, 11, 15, ]
result = reduce(lambda x, y: x * y, numbers)
print(result)  # 11404800
```

Explanation of the above function:

function: `lambda x, y: x * y`

- step1: `lambda` => `1 * 12` = `12`
- step2: `lambda` => `12 * 30` = `360`
- step3: `lambda` => `360 * 24` = `8640`
- step4: `lambda` => `8640 * 8` = `69120`
- step5: `lambda` => `69120 * 11` = `760320`
- step6: `lambda` => `760320 * 15` = `11404800`

> **Note**: We might mistakenly think that we could find out sum of squares with
> the `reduce` function by passing lambda as `lambda x,y: x**2 + y**2` but it
> end up giving very large number since it finds out square of first 2 numbers
> and in the next iteration, it again finds out the square of the past result
> and add it with the square of the next occurrence.

Explanation:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x ** 2 + y ** 2, numbers)
print(result)  # 1373609

```

here we might think that the reduce function does `1 + 4 + 9 + 16 + 25` but it
does something like below:

`[{(1 + 4) ** 2 + 9} ** 2 + 16] ** 2 + 25` which will be equal to `1373609`

- step 1: `lambda` => `1 ** 2 + 2 ** 2` = `1 + 4` = `5`
- step 2: `lambda` => `5 ** 2 + 3 ** 2` = `25 + 9` = `34`
- step 3: `lambda` => `34 ** 2 + 4 ** 2` = `1156 + 16` = `1172`
- step 4: `lambda` => `1172 ** 2 + 5 ** 2` = `1,373,584 + 25` = `1373609`
