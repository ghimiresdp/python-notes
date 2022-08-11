- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

[go to course contents](https://github.com/ghimiresdp/python-level1/)
<hr>

# Chapter 6.3: Arbitrary arguments in python

**Table of Contents:**
- [Chapter 6.3: Arbitrary arguments in python](#chapter-63-arbitrary-arguments-in-python)
    - [Background](#background)
    - [Arbitrary number of arguments](#arbitrary-number-of-arguments)
    - [Arbitrary number of keyword arguments](#arbitrary-number-of-keyword-arguments)

## Background
As our functions become more and more dynamic, it is not possible to define a
function with maximum number of default arguments which makes our code more
complicated. Example, we want to be able to add either 3, or 4, or 5 or even
10 arguments.

**The Traditional Approach:**
```python
def add_numbers(a, b, c=0, d=0, e=0, f=0, g=0):
    return a + b + c + d + e + f + g

print(add_numbers(1,2)) # 3
print(add_numbers(1,2, 3))   # 6
print(add_numbers(1,2, 3, 4))   # 10
print(add_numbers(1,2, 3, 4, 5))    # 15
print(add_numbers(1,2, 3, 4, 5, 6)) # 21
```
Here, the main problem is default parameters in all optional values which even
decreases the code readability. If we could pass dynamic number of arguments,
then we did not need to set default values to each variable.

## Arbitrary number of arguments

In the above scenario, if we use arbitrary number of arguments, then we could do
the following:

```python
def add_numbers(a, b, *args):
    sum_value = a + b
    for item in args:
        sum_value += item
    return sum_value
print(add_numbers(1, 2)) # 3
print(add_numbers(1, 2, 3))   # 6
print(add_numbers(1, 2, 3, 4))   # 10
print(add_numbers(1, 2, 3, 4, 5))    # 15
print(add_numbers(1, 2, 3, 4, 5, 6)) # 21
```
Here, add_number needs at lease 2 numbers to calulate the sum but is capable of
accepting any number of arguments and perform addition

## Arbitrary number of keyword arguments
