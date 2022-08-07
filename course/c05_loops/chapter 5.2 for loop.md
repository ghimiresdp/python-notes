- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

[go to course contents](https://github.com/ghimiresdp/python-level1/)
<hr>

# Chapter 5.2: For Loop

**Table of Contents:**
- [Chapter 5.2: For Loop](#chapter-52-for-loop)
- [Introduction to For Loop](#introduction-to-for-loop)
    - [The Range Function](#the-range-function)
    - [Using For loop with string, list, tuple, set, and dictionary](#using-for-loop-with-string-list-tuple-set-and-dictionary)
- [Nested For Loop](#nested-for-loop)

# Introduction to For Loop
A For Loop iterates over a sequence of items over the iterable in the order that
they appear in a sequence. While `while` loops generally use the conditions for
breaking out of the loop, `for` loops have definite number of items to iterate
over. Generally, We use generator function (eg: `range()`) to
create a sequence of numbers and loop over them to achieve loop for n-times.

## The Range Function
The `range()` function creates a range of numbers through which, we can iterate
over using for loop. The `range()` function is a generator which *yields* an
item at a time rather than returning the whole sequence of numbers which saves
a lot of memory when generating a sequence of millions of items.

**Example 1:**
```python
range(10)       # creates a range from 0 upto 9
range(1, 10)    # creates a sequence of numbers from 1 to 10
range(1, 10, 2) # createa a sequence of numbers from 1 to 10 with step of 2
```

**Example 2:** Using `range()` function to iterate for 10 times
```python
for x in range(10):
    print(f'The current value of x is: {x}')
```

**Output**
```
The current value of x is: 1
The current value of x is: 2
The current value of x is: 3
The current value of x is: 4
The current value of x is: 5
The current value of x is: 6
The current value of x is: 7
The current value of x is: 8
The current value of x is: 9
```

**Example 3:** different usage of `range()` function.
```python
# generating odd numbers from 1 upto 19
odd = list(range(1, 20, 2))
print(odd)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# Generating multiples of 3
multiples = list(range(3, 31, 3))
print(multiples)
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

```

## Using For loop with string, list, tuple, set, and dictionary


##
# Nested For Loop

#
