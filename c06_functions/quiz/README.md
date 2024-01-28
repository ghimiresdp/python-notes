# Chapter 6 Functions Quiz

Please read the note carefully and try to solve the problem below:

**Table of Contents**:

- [Chapter 6 Functions Quiz](#chapter-6-functions-quiz)
  - [Quiz Q0601 _largest number_](#quiz-q0601-largest-number)
  - [Quiz Q0602 _upper case characters count_](#quiz-q0602-upper-case-characters-count)
  - [Quiz Q0603  _coffee specialist_](#quiz-q0603--coffee-specialist)
  - [Quiz Q0604 _multiplication table_](#quiz-q0604-multiplication-table)
  - [Quiz Q0605 _palindrome_](#quiz-q0605-palindrome)
  - [Quiz Q0606 _sorted word_](#quiz-q0606-sorted-word)
  - [Quiz Q0607 _linear equation_](#quiz-q0607-linear-equation)
  - [Quiz Q0608 _multiply or divide and add_](#quiz-q0608-multiply-or-divide-and-add)
  - [Quiz Q0609 _lambda_](#quiz-q0609-lambda)
  - [Quiz Q0610 _lambdas_](#quiz-q0610-lambdas)
  - [Quiz Q0611   _recursion_](#quiz-q0611---recursion)

> **Note**:
>
> please refer to the repository
> **[python projects](https://github.com/ghimiresdp/python-projects)** for more
> exercises and projects related to this chapter.
>

## Quiz Q0601 _largest number_

Write a python function to find the largest out of 3 numbers.
You should use comparison operator to find out the maximum of 3 numbers.

## Quiz Q0602 _upper case characters count_

Write a python function that calculates the number of upper case characters, lower case characters and spaces in the string and returns them as a tuple.

For example: We have a string as `"Hello World"`. The function should be able to return `(2, 8, 1)` where the first element is the count of Upper case characters, the second element is the count of lower case characters and third element is the count of spaces.

## Quiz Q0603  _coffee specialist_

Suppose you went to a coffee shop. A shopkeeper asked you to create a program that serves coffee according to the customer's requirements.

The coffee machine should ask user to enter any numbers below that should make a coffee and serve it to the user.
Please use the function `make_coffee()` to prepare a coffee and serve it.

Followings are the ingredients for coffee:

- **Sugar**: no. of spoons  `int`
- **Beans**: no. of spoons  `int`
- **Milk**: volume in ml.   `int`

The total volume of coffee should be `250ml`. The maximum volume of milk can be only up to  `150ml`. The volume Greater than the limit
should give the error saying not acceptable.

Finally print the line describing the coffee you prepared along with  milk and water composition.

## Quiz Q0604 _multiplication table_

Write a program to create a multiplication table of the given number.
The `mul_table()` function should have the following arguments:

- **number** `int`: the number to print multiplication table of.
- **limit** `int`: the number up to which multiples are printed (which should have the default value of 10).

Example multiplication table for 13 should look similar to the output below:

```
| 13  X   1 |    13 |
| 13  X   2 |    26 |
| 13  X   3 |    39 |
| 13  X   4 |    52 |
| 13  X   5 |    65 |
| 13  X   6 |    78 |
| 13  X   7 |    91 |
| 13  X   8 |   104 |
| 13  X   9 |   117 |
| 13  X  10 |   130 |
```

## Quiz Q0605 _palindrome_

Write a function that takes a string and checks whether the word is palindrome or not.

- A palindrome is a string that reads the same backward or forward.
- Examples: `eve`, `dad`, `rotator`

Your program should be able to ask user to enter the word and check whether it is palindrome or not. The program should not end until user enters `no`.

The output should show inside a box as shown below with text justified center.

```
===================[ Palindrome Finder ]===================
Enter a word: rotator

+---------------------------------------------------------+
|           The word 'rotator' is a palindrome            |
+---------------------------------------------------------+

The word 'rotator' is a palindrome word

Do you want to check again? [yes/no]: yes

Enter a word: dad

+---------------------------------------------------------+
|             The word 'dad' is a palindrome              |
+---------------------------------------------------------+


Do you want to check again? [yes/no]: no

======================[ exiting now ]=====================
```

## Quiz Q0606 _sorted word_

Write a function that accepts words that are separated by hyphen returns the alphabetically sorted words
separated by hyphen.

Hint:

- split the words using `string.split()` method
- sort the list
- join the list to a string with `string.join()` method

Example snippet for the problem is as follows:

```python
word = "cat-apple-dog-ball-ears-goose-fish"
def sort_words(word: str):
    # change your function body here
    return sorted_word

sorted_words = sort_words(word)
print(sorted_words)
# "apple-ball-cat-dog-ears-fish-goose"
```

## Quiz Q0607 _linear equation_

Write a function that accepts a number `x`

- If `x` is a multiple of `2`, it should return the value `y` = `x**2 + 2x + 3`
- If `x` is a multiple of `3`, it should return the value `y` = `x**3 + 4x + 5`
- If `x` is a multiple of both `2` and `3`, it should return the value `y` = `x**3 + 4x**2 + 5x + 6`
- In other cases it should return negative value of the given number

## Quiz Q0608 _multiply or divide and add_

Write a function that accepts any number of arguments
find out the sum of all numbers by multiplying by `2` if it is odd and dividing by `2` if it is even.

Example:  if arguments are `(5,6,7,8)`, then the result should be `31` (5 _2 + 6 / 2 + 7_ 2 + 8 / 2)

## Quiz Q0609 _lambda_

Convert the following function to a lambda function

```python
def odd_or_even(num):
    if num%2==0:
        return 'even'
    else:
        return 'odd'
```

## Quiz Q0610 _lambdas_

Create lambda functions for the following:

1. A lambda function that accepts a number and returns the square of it.
2. A lambda function that accepts a list of numbers and returns the list of squares of them
3. A lambda function that accepts the length in meter and returns the value in feet.
4. A lambda function that accepts 3 integer arguments for month, year, and day, and returns a single string in format `YYYY/MM/DD` format.
5. A lambda that accepts a sentence and returns the sentence with spaces replaced by hyphens.

   ``` python
   # example
   input_sentence = 'A quick brown fox jumps over the lazy dog.'

   output_sentence = 'A-quick-brown-fox-jumps-over-the-lazy-dog.'
   ```

## Quiz Q0611   _recursion_

Write recursive functions to find out the following:

1. sum of first n natural numbers
2. factorial of a non-negative number
3. sum of digits of the number
4. print the nth element of the fibonacci series `[1, 1, 2, 3, 5, 8, 13, 21,...]`
