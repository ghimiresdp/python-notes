# Chapter 5 Loop Quiz
https://sudipghimire.com.np

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
3. If each item of a list is represented by `x`, evaluate the value y = $x ^ 2$ + $2x$ + $2$ where `y` is the resulting expression for each item of the list.
4. Find the average of the list.


## Quiz Q0504
Write a program that accepts a number from a user and finds out all the positive factors of the number. The program should terminate if user provides any number less than 1.

_Factor is a number that divides the given number without giving remainders._

Examples:

- **factors of `10` are**:  `1`, `2`, `5`, and `10`
- **factors of `18` are**:  `1`, `2`, `3`, `6`, `9` and `18`


## Quiz Q0505

Write a program to check whether a number is a special number or not.

   If the sum of the *factorial* of digits of a number (N) is equal to the number itself,
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
