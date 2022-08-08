- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

[go to course contents](https://github.com/ghimiresdp/python-level1/)
<hr>

# Chapter 5.4: Comprehensions

**Table of Contents**
- [Chapter 5.4: Comprehensions](#chapter-54-comprehensions)
    - [List Comprehension](#list-comprehension)
    - [List Comprehension With if condition](#list-comprehension-with-if-condition)
    - [Dictionary Comprehension](#dictionary-comprehension)

## List Comprehension
List Comprehension creates a new list by applying an expression to each element
of an iterable.


Basic Syntax:
```python
iterable = [<expression> for <element> in <iterable>]
```

**Example 1:**
```python
lst_1 = [x*2 for x in range(1, 11)]

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

**Example 2:**

```python
word = 'Hello World'
ascii_values = [ord(char) for char in word]

# [72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]
```


## List Comprehension With if condition
List Comprehension with if condition is used to filter and perform operations
if needed from another iterable.

**Syntax**
```python
[<expression> for <element> in <iterable> if <condition>]
```

**Example 1:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7]

even  = [num for num in numbers if num%2 == 0]
# [2, 4, 6]
```

## Dictionary Comprehension

**Example 1:**
```python
dict_1 = {key: key**2 for key in range(1, 6)}

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
