# Chapter 5.4: Comprehensions

**Table of Contents**:

- [Chapter 5.4: Comprehensions](#chapter-54-comprehensions)
  - [List Comprehension](#list-comprehension)
  - [List Comprehension With if condition](#list-comprehension-with-if-condition)
  - [Set Comprehension](#set-comprehension)
  - [Dictionary Comprehension](#dictionary-comprehension)
  - [Generator Comprehension](#generator-comprehension)

## List Comprehension

List Comprehension creates a new list by applying an expression to each element
of an iterable.

Basic Syntax:

```python
iterable = [<expression> for <element> in <iterable>]
```

**Example 1:**

```python
# Regular method
new_list = []
for x in range(1, 11):
    new_list.append(x*2)
print(new_list)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# List Comprehension
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

**Syntax**:

```python
[<expression> for <element> in <iterable> if <condition>]
```

**Example 1:**

```python
numbers = [1, 2, 3, 4, 5, 6, 7]

even  = [num for num in numbers if num%2 == 0]
# [2, 4, 6]
```

## Set Comprehension

Set Comprehension is similar to list comprehension, but uses curley brackets
and can not contain duplicate values.
**Syntax**

```python
value = {<expression> for <item[s]> in iterable}
```

**Example:**

```python
my_set = {value**3 for value in range(5, 12)}
print(my_set)

# {512, 1000, 1331, 343, 216, 729, 125}
```

## Dictionary Comprehension

**Syntax**:

```python
value = {<key_expression>: <value_expression> for <item[s]> in iterable}
```

**Example 1:**

```python
dict_1 = {key: key**2 for key in range(1, 6)}

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Generator Comprehension

As List Comprehension does an eager execution, it will be computationally
inefficient and will use more memory. So if we want to optimize our system to
use less memory and perform computation whenever required, we can comprehend
generators.

A generator comprehension is similar to the list comprehension. Only the
difference is the notation `()` instead of `[]`

**Example:** Using List Comprehension

```python
# Using List Comprehension to get first 1000 squares
squares = [x ** 2 for x in range(1000)]
print(squares.__sizeof__())     # 8840

# Using List Comprehension to get first 1000000 squares
squares_1 = [x ** 2 for x in range(1000000)]
print(squares_1.__sizeof__())     # 8448712
```

**Example:** Using Generator Comprehension

```python
# Using Generator Comprehension to get first 1000 squares
squares = (x ** 2 for x in range(1000))
print(squares.__sizeof__())   # 96

# Using Generator Comprehension to get first 1000000 squares
squares_1 = (x ** 2 for x in range(1000000))
print(squares_1.__sizeof__())   # 96
```

In above example, we can see the generator comprehension takes only `96 bytes`
of memory in both cases while the list comprehension takes `8.8 KB` of memory
by `squares` whereas `84.4MB` of memory by `squares_1`.
