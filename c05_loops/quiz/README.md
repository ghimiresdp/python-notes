# Chapter 5 Loop Quiz

**Table of contents**:

- [Chapter 5 Loop Quiz](#chapter-5-loop-quiz)
  - [Quiz Q0501](#quiz-q0501)
  - [Quiz Q0502](#quiz-q0502)
  - [Quiz Q0503](#quiz-q0503)
  - [Quiz Q0504](#quiz-q0504)
  - [Quiz Q0505](#quiz-q0505)
  - [Quiz Q0606](#quiz-q0606)
    - [Pattern 1](#pattern-1)
    - [Pattern 2](#pattern-2)
    - [Pattern 3](#pattern-3)
    - [Pattern 4](#pattern-4)
    - [Pattern 5](#pattern-5)
    - [Pattern 6](#pattern-6)
    - [Pattern 7](#pattern-7)
    - [Pattern 8](#pattern-8)
    - [Pattern 9](#pattern-9)
    - [Pattern 10  (Bonus Exercise)](#pattern-10--bonus-exercise)
  - [Quiz Q0607](#quiz-q0607)
  - [Quiz Q0608](#quiz-q0608)

Please read the note carefully and try to solve the problem below:

**Note**: _Some of the symbols in the text below are available in the markdown preview mode only so if you are using a regular text editor, please prefer visual studio code and see the question in preview mode or github preview mode._

## Quiz Q0501

From the list below, separate a list that are even and odd and put them into the respective variables

``` python
num = [1, 5, 2, 89, 32, 112, 167, 333, 20, 5, 23]
odd_num = []
even_num=[]
```

the final output should be:

```
Odd numbers: [1, 5, 89, 167, 333, 5, 23]
Even numbers: [2, 32, 112, 20]
```

## Quiz Q0502

Write a program to print the first 20 fibonacci numbers

The fibonacci sequence is a sequence of numbers where the next number in the sequence is
the sum of the previous two numbers in the sequence.
eg: `1, 1, 2, 3, 5, 8, 13, ...`

hint: use for loop in range of 20, add a and b and update values of a, b and others if necessary

``` python
a = 1
b = 1
# answer here
```

## Quiz Q0503

Write a program to create a list of 100 Natural numbers.

1. Find the sum of all numbers from the list using `for` loop.
2. Find the sum of squares of all numbers from the list using `for` loop.
3. If each item of a list is represented by `x`, evaluate the value y = `x**2 + 2x + 2` where `y` is the resulting expression for each item of the list.
4. Find the average of the list.

## Quiz Q0504

Write a program that accepts a number from a user and finds out all the positive factors of the number. The program should terminate if user provides any number less than 1.

_Factor is a number that divides the given number without giving remainders._

Examples:

- **factors of `10` are**:  `1`, `2`, `5`, and `10`
- **factors of `18` are**:  `1`, `2`, `3`, `6`, `9` and `18`

## Quiz Q0505

Write a program to check whether a number is a special number or not.

   If the sum of the _factorial_ of digits of a number (N) is equal to the number itself,
   the number (N) is called a special number.

Eg: `145` is a special number where, `1! + 4! + 5!` = `145`

**Hint 1**: _you can get each digit using a `modulus` and `integer division` of a number by `10` until the number is less than `10`_.

Let us take a number `145`:
| Steps | integer division by 10 | Modulus by 10  | remarks               |
| ----: | ---------------------- | -------------- | --------------------- |
|     1 | `145 // 10 = 14`       | `145 % 10 = 5` | `5` is ones digit     |
|     2 | `14 // 10 = 1`         | `14 % 10 = 4`  | `4` is tens digit     |
|     3 | at the end, 1          | `1 % 10 = 1`   | `1` is hundreds digit |

**Hint 2**: _you can use `math.factorial()` to find out factorial of a number_.

## Quiz Q0606

Generate patterns below using nested loops:

### Pattern 1

```
*
*   *
*   *   *
*   *   *   *
*   *   *   *   *
```

### Pattern 2

```
1
1   3
1   3   5
1   3   5   7
1   3   5   7   9
```

### Pattern 3

```
1
2   2
3   3   3
4   4   4   4
5   5   5   5   5
```

### Pattern 4

```
1
2   1
3   2   1
4   3   2   1
5   4   3   2   1
```

### Pattern 5

```
1   2   3   4   5
2   4   6   8   10
3   6   9   12  15
4   8   12  16  20
5   10  15  20  25
```

### Pattern 6

```
A
A   P
A   P   P
A   P   P   L
A   P   P   L   E
```

### Pattern 7

```
                *
            *   *
        *   *   *
    *   *   *   *
*   *   *   *   *
```

### Pattern 8

```
                1
            1   3
        1   3   5
    1   3   5   7
1   3   5   7   9
```

### Pattern 9

```
                A
            A   P
        A   P   P
    A   P   P   L
A   P   P   L   E
```

### Pattern 10  (Bonus Exercise)

```
                1
            1   2   1
        1   2   3   2   1
    1   2   3   4   3   2   1
1   2   3   4   5   4   3   2   1
```

## Quiz Q0607

1. Convert the following loop to list comprehension

```python
lst = []
for x in range(10):
    lst.append(2*x+1)
```

2. Generate a dictionary from a list of first 10 numbers and it's square values using dictionary comprehension.

   Final value should be similar to: {1:1, 2:4, 3:9, 4:16, ..., 10, 100}

3. Create the following pattern using list comprehension, `join()` method, and others if needed. Try to solve in a single line or single statement.

```
1
1   2
1   2   3
1   2   3   4
1   2   3   4   5
```

4. A mathematical function is defined by y = `4x ** 2 + 3x - 6`
    1. Create a generator function to generate first 1000 integers starting from -100 and store to a variable y.
    2. Create a list using list comprehension to generate the same values
    3. Compare the memory usage by those variables created in steps `i` and `ii` using `__sizeof__()` method.
    4. Try to generate values of y for first million integers and compare memory usage as done in step `iii`.

    To learn more about `__sizeof__()` method, please visit <https://www.javatpoint.com/sizeof-in-python>

5. Write a program to split a string `'Apple'` into a dictionary of _ASCII_ values of each characters using **comprehension** methods.
    - To learn more about ASCII please refer to the site <https://www.asciitable.com/>
    - Use the `ord()` method to find out the ASCII values
    - The final output should be:

        ```
        {'A': 65, 'p': 112, 'l': 108, 'e': 101}
        ```

6. Write a program to generate a dictionary from the given nested tuple using dictionary comprehension.

```python
abbreviations = (
    ('ABC', 'Atanasoff Berry Computer'),
    ('BCD', 'Binary Coded Decimal'),
    ('CD', 'Compact Disc'),
    ('DVD', 'Digital Video Disc'),
    ('HTTP', 'Hyper Text Transfer Protocol'),
    ('WWW', 'World Wide Web'),
)
```

## Quiz Q0608

Try pattern generation exercises from [Quiz Q0606](#quiz-q0606) if possible with list comprehension methods.
