# Chapter 2.5. Basic Operations

**Table of Contents**:

- [Chapter 2.5. Basic Operations](#chapter-25-basic-operations)
  - [arithmetic operations](#arithmetic-operations)
    - [Addition ( `+` )](#addition---)
    - [Subtraction ( `-` )](#subtraction----)
    - [Multiplication ( `*` )](#multiplication---)
    - [Division ( `/` )](#division---)
    - [Modulus ( `%` )](#modulus---)
    - [Exponentiation ( `**` )](#exponentiation---)
    - [Integer Division ( `//` )](#integer-division---)
  - [Relational Operations](#relational-operations)
    - [equals ( `==` )](#equals---)
    - [not equals ( `!=` )](#not-equals---)
    - [less than ( `<` )](#less-than---)
    - [less than or equals ( `<=` )](#less-than-or-equals---)
    - [greater than ( `>` )](#greater-than---)
    - [greater than or equals ( `>=` )](#greater-than-or-equals---)
  - [logical operations](#logical-operations)
    - [`and` operation](#and-operation)
    - [`or` operation](#or-operation)
    - [`not` operation](#not-operation)
    - [Compound logical operations](#compound-logical-operations)
  - [identity operations](#identity-operations)
  - [membership operations](#membership-operations)
  - [bitwise operations](#bitwise-operations)
    - [Bitwise AND `&`](#bitwise-and-)
    - [Bitwise OR `|`](#bitwise-or-)
    - [Bitwise XOR `^`](#bitwise-xor-)
    - [Bitwise NOT `~`](#bitwise-not-)
    - [Bitwise shift left `<<`](#bitwise-shift-left-)
    - [Bitwise shift right `>>`](#bitwise-shift-right-)
  - [assignment operations](#assignment-operations)

## arithmetic operations

Arithmetic operations includes the basic arithmetic operations to different data types. The following are the basic
arithmetic operations

### Addition ( `+` )

**Syntax**: `a + b`

```python
a1 = 5 + 6  # integer and integer
a2 = 5.5 + 2.3  # float and float
a3 = 4.7 + 2  # integer and float
a4 = "Hello " + "world"  # string and string
a5 = (5 + 4j) + (6 + 5j)  # complex and complex
```

### Subtraction ( `-` )

**Syntax**: `a - b`

```python
b1 = 5 - 6  # integer and integer
b2 = 5.5 - 2.3  # float and float
b3 = 4.7 - 2  # integer and float
# b4 = "Hello " - "world"  # string subtraction not supported
b5 = (5 + 4j) - (6 + 5j)  # complex and complex
```

### Multiplication ( `*` )

**Syntax**: `a * b`

```python
c1 = 5 * 6  # integer and integer
c2 = 5.5 * 2.3  # float and float
c3 = 4.7 * 2  # integer and float
c4 = "Hello " * 5  # string and int
c5 = (5 + 4j) * (6 + 5j)  # complex and complex
```

### Division ( `/` )

**Syntax**: `a / b`

```python
d1 = 5 / 6  # integer and integer
d2 = 5.5 / 2.3  # float and float
d3 = 4.7 / 2  # integer and float
d4 = (5 + 4j) / (6 + 5j)  # complex and complex
```

### Modulus ( `%` )

Modulus operation finds out the remainder whenever the number is divided by
another number. for example if `10` is divided by `3`, it gives remainder `1`.

**Syntax**: `a % b`

```python
e1 = 55 % 4  # integer and integer      gives: 3
e2 = 5.5 % 2.3  # float and float
e3 = 4.7 % 2  # integer and float
```

### Exponentiation ( `**` )

Exponentiation is also known as power. In python we can find out the
n<sup>th</sup> power of a number using `**` symbol. example  `10 ** 2` means 10<sup>2</sup> = 100.

**Syntax**: `a ** b`

```python
f1 = 5 ** 4  # integer and integer
f2 = 5.5 ** 2.3  # float and float
f3 = 4.7 ** 2  # integer and float
```

### Integer Division ( `//` )

Integer division always gives the integer equivalent value of the result when
a number is divided by another. For example `10/4` is `2.5` but the integer
division gives out the integer part only i.e. `10 // 4` gives `2`.

**Syntax**: `a // b`

```python
print(5 // 2)
g1 = 45 // 2
g2 = 45.8 // 5.1  # 8.0   # integer equivalent of float

```

## Relational Operations

Relational operations or comparison operations compare 2 values and returns either `True` or `False`. When
comparing `less than` or `greater than` in strings or sequences, it compares the ASCII value using lexicographical
ordering.

### equals ( `==` )

```python
print(5 == 6)  # False
print(4 + 1 == 6 - 1)  # True
print('John' == 'John')  # True
```

### not equals ( `!=` )

```python
print(5 != 6)  # True
print(4 + 1 != 6 - 1)  # False
print('John' != 'John')  # False

```

### less than ( `<` )

```python
print(4 < 5)  # True
print(4 < 4)  # False
print(5 < 4)  # False
print('Jane' < 'John')  # True

```

### less than or equals ( `<=` )

```python
print(4 <= 5)  # True
print(4 <= 4)  # True
print(5 <= 4)  # False
print([1, 2, 3] <= [1, 3, 2])  # True

```

### greater than ( `>` )

```python
print(4 > 5)  # False
print(4 > 4)  # False
print(5 > 4)  # True
print('Jane' > 'John')  # False
print([1, 2, 3] > [1, 3, 2])  # False

```

### greater than or equals ( `>=` )

```python
print(4 >= 5)  # False
print(4 >= 4)  # True
print(5 >= 4)  # True
print('A' >= 'B')  # False
```

## logical operations

Logical operations are performed on boolean values. The following are logical operations available in python.

### `and` operation

- **Syntax**: `[value_1] and [value_2]`
- returns true when both `value_1` and `value_2` are `True`.

```python
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
```

An another example

```python
is_married = True
has_children = False
is_life_complete = is_married and has_children

print(is_life_complete)  # False
```

### `or` operation

- **Syntax**: `[value_1] or [value_2]`
- returns true when any or all of `value_1` and `value_2` are `True`.

```python
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
```

an another example:

```python
is_father_rich = True
has_high_income = False
is_rich = is_father_rich or has_high_income

print(is_rich)  # True
```

### `not` operation

- **Syntax**: `not [value]`
- returns the negative of the `value`.

```python
print(not True)  # False
print(not False)  # True

is_work = False
print(not is_work)  # True
```

### Compound logical operations

We can combine multiple logical operations to form a compound logical operation. We use compound logical operation to
perform advanced operations. We generally use brackets to combine multiple logical operations.

some example are shown below:

```python
print(True or False or True)  # True
print(True and False or False and True)  # False

# in some conditions, use of brackets alter the expected result
print(not True or not False)  # True
print(not (True or not False))  # False
print((not True) or (not False))  # True
```

another example:

``` python
# if it is cloudy today and if it rained yesterday, then it rains today
# in other conditions it doesn't rain
cloudy = False
rained = True

rains = cloudy and rained

if rains:
    print("it rains today")
else:
    print("It does not rain today")

# it does not rain today
```

## identity operations

Identity operation compares whether 2 objects are same objects or not. Remember,
They are not used to compare for equality. There are 2 basic identity operations

1. `is`
2. `is not`

```python
print(type('abc') is str)  # True
```

```python
list1 = ['abc', 'def']
list2 = list1  # same object is referenced here
list3 = list1.copy()  # shallow copy is made here

print(list1 is list2)  # True
print(list1 is list3)  # False

print(type(list1) is not int)  # True

```

**Note**: Sometimes, we use identity operations in wrong places. for example:

```python
print((1 + 4) is (6 - 1))
```

The above statement gives the equality, but still shows warning suggesing `==`
instead of `is` operator.

## membership operations

Membership Operation checks if an element is present in the specified object
or collection or not.

Basic Membership Operators:

- `in`
- `not in`

Example 1:

```py
sentence = 'A quick brown fox jumps over the lazy dog.'
print('fox' in sentence)  # True
print('monkey' in sentence)  # False

print('fox' not in sentence)  # False
print('monkey' not in sentence)  # True

```

Example 2:

```py
x = [1, 2, 3, 4, 5]
print(5 in x)  # True
print(10 in x)  # False

print(2 not in x)  # False
print(20 not in x)  # True
```

## bitwise operations

Bitwise operation, as suggested by name, work on bits. They work only with
numeric values (specifically integers) since we need to convert the number to
corresponding binary equivalent to perform operation. Bitwise operation is done
on a bit-by-bit rather than a number as a whole.

For example: If we want to perform bitwise operation on 9 and 26, then we need
to convert them to the equivalent binary representation.

- The binary equivalent of `9` is `01001`.
- The binary equivalent of 26 is `011010`.

If the number of bits between 2 numbers are not equal to perform operations,
the number with less number of bits is automatically zero-padded.

Example:

```
Positive numbers are preceed by by 0
 26  = 0 1 1 0 1 0  =   [0] 1 1 0 1 0
  9  =   0 1 0 0 1  =   [0] 0 1 0 0 1

Negative numbers are preceed by by 1
(representation might be different on different programming languages)
-10  =   1 0 1 1 0  =   [1] 0 1 1 0
```

> **Note**:
>
> - _1's complement of `1010` is `0101`._
> - _2's complement of `1010` is `0101` + `1` = `0110`._
> - _Number starting with `0` represents the positive number_
> - _Number starting with `1` represents the negative number_

Now, each bit of a number is performed logical operation with the same position
of another number.

- The unit digit of 26 interacts with the unit digit of 9.
- The second digit of 26 interacts with the second digit of 9.
- ...
- The foremost digit of 26 interacts with the foremost (padded) digit of 9.

The following are bitwise operations supported in python:

### Bitwise AND `&`

This operation performs logical `AND` operations on each bits of 2 numbers

```py
print(9 & 26)   # 8
```

Explanation:

```
26    = 0 1 1 0 1 0
 9    = 0 0 1 0 0 1
_________________________
AND   = 0 0 1 0 0 0  = 8
 ```

### Bitwise OR `|`

This operation performs logical `OR` operations on each bits of 2 numbers

```py
print(9 | 26)   # 27
```

Explanation:

```
26    = 0 1 1 0 1 0
 9    = 0 0 1 0 0 1
_________________________
OR    = 0 1 1 0 1 1  = 27
 ```

### Bitwise XOR `^`

This operation performs logical `XOR` operations on each bits of 2 numbers

```py
print(9 ^ 26)   # 19
```

Explanation:

```
26    = 0 1 1 0 1 0
 9    = 0 0 1 0 0 1
_________________________
XOR   = 0 1 0 0 1 1  = 19
```

### Bitwise NOT `~`

Bitwise `NOT` operation is performed on a single variable since it negates all
the bits of the given number. remember, the representation of negative number is
a bit weird than a regular positive integer.

```py
print(~9)   # -10
```

Explanation:

```
 9    = 0 1 0 0 1
_________________________
NOT   = 1 0 1 1 0  = -10
 ```

> **Note**: _To understand the negative number, you need to understand:_
>
> - 1's Complement
> - 2's Complement

### Bitwise shift left `<<`

This process shifts all bits towards the left by specified number of times. The
bit-wise shift left doubles the number for each shift.

Example:

```py
print(6 << 1)   # 12
print(6 << 2)   # 24
```

Explanation:

```
   6  = |     0 1 1 0 |        We can prepend any number of zeros for positive.
<< 1  = |   0 1 1 0 _ |        the vacant place is padded with zero
      = |   0 1 1 0 0 |  = 12  (6 << 1)
<< 1  = | 0 1 1 0 0 0 |  = 24  (6 << 2)

```

### Bitwise shift right `>>`

This process shifts all bits towards the right by specified number of times. The
bit-wise shift right halves the number (with integer division) for each shift.

Example:

```py
print(6 >> 1)   # 3
print(6 >> 2)   # 1
```

Explanation:

```
   6  = | 0 1 1 0 |
>> 1  = | _ 0 1 1 | 0          the right-most value (0) is discarded
      = | _ 0 1 1 | x     = 3   (6 >> 1)
>> 1  = | _ _ 0 1 | 1     = 1  the right-most value (1) is discarded
      = | _ _ 0 1 | X     = 1  (6 >> 2)

```

## assignment operations

Assignment Operations assign values from right side operands to left side
operand/operands. Following are assignment operations used in python:

1. `=`
    - example: `x = 5`

2. `+=`
    - example: `x += 5`
    - equivalent code: `x = x + 5`

3. `-=`
    - example: `x -= 5`
    - equivalent code: `x = x - 5`

**Other assignment operations:**

1. `*=`
2. `/=`
3. `%=`
4. `//=`
5. `**=`
6. `&=`
7. `|=`
8. `^=`
9. `>>=`
10. `<<=`
