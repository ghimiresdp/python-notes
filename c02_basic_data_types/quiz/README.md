# Chapter 2 Data Types Quiz

Please read the note carefully and try to solve the problem below:

**Table of Contents**:

- [Chapter 2 Data Types Quiz](#chapter-2-data-types-quiz)
  - [Quiz Q0201](#quiz-q0201)
  - [Quiz Q0202](#quiz-q0202)
  - [Quiz Q0203](#quiz-q0203)
  - [Quiz Q0204](#quiz-q0204)
  - [Quiz Q0205](#quiz-q0205)
  - [Quiz Q0206](#quiz-q0206)
  - [Quiz Q0207](#quiz-q0207)
  - [Quiz Q0208](#quiz-q0208)
  - [Quiz Q0209](#quiz-q0209)
  - [Quiz Q0210](#quiz-q0210)
  - [Quiz Q0211](#quiz-q0211)

## Quiz Q0201

1. Assign `55` to the variable `x` and print it in the console
2. change the value of variable to be `60`
3. add x by `10` again and print the value.

**[Click](solution/q0201.py)** to see the solution

## Quiz Q0202

1. create a variable `x` and assign any _integer_ value in it
2. create a variable `y` and assign any _float_ value in it
3. try using function `type()` for x and y to check its data type.

```python
# Examples
type(x)
type(4.5)
```

**[Click](solution/q0202.py)** to see the solution

## Quiz Q0203

Create two variables `first_name`, and `last_name` and print the sentence in the format below:

`"My name is John Doe"`

1. use `+` operator to concatenate strings
2. use `format()` method to achieve the same result
3. use _f-strings_ to achieve the same result
4. use `%s` formatting method to achieve the same result

**[Click](solution/q0203.py)** to see the solution

## Quiz Q0204

Assign a variable  pi and assign value `3.14159265`

1. use _formatting strings_ to show pi with 3 digits after the decimal
2. use _formatting strings_ to show pi with 2 digits after the decimal but allocate 10 spaces for the variable.
3. use f-string to show the result in the following format:
    "The value of PIE is        3.14" ( hint: `"%<a>.<b>f"` )

**[Click](solution/q0204.py)** to see the solution

## Quiz Q0205

Use a function `input()`  to input the the name and age from the command line and display the formatted text as instructed below:

1. use `input()` function to ask the name to the user. The console should show `"What is your name?"` to input the name
2. similarly ask the user to input the _age_ and assign it to another variable.
3. Show a sentence describing the user name and age using _different formatting methods_.
   - hint: Output would be a sentence similar to `Hello 20 years old John!!`.

**[Click](solution/q0205.py)** to see the solution

## Quiz Q0206

Perform the addition operations between the following data types and check whether the code runs successfully or not:

1. `int` and `int` (Example: `5 + 5`)
2. `int` and `float` (Example: `5 + 5.5`)
3. `float` and `float` (Example: `5.5 + 5.5`)
4. `str` and `str` (Example: `'hello' + 'world'`)
5. `int` and `str` (Example: `5 + 'hello'`)

## Quiz Q0207

Use different operations in python to find out the following:

1. Square of **10**
2. **10<sup>20</sup>**
3. Integer division of **100** by **30**
4. What would be the remainder if 1289 is divided by 25? solve programmatically.

## Quiz Q0208

The following variables are assigned values as below:

```python
x = 10
y = 12
```

1. Check if x is greater than y
2. Check if y is greater than x
3. check if x is greater than or equal to y
4. check if y is greater than or equal to x
5. Check if x becomes equal to y if x is added by 2
6. Check if x is not equal to y after the previous operation

## Quiz Q0209

_"If the weather is cloudy today and it rained yesterday, it will rain today"_.

Generate the logical operation for the statement above and evaluate the weather forecast for today.

```python cloudy_today = True rained_yesterday = True
```

**Note**: _Change parameters to different values and see when the result changes_

## Quiz Q0210

Use _Identity_ and _Membership_ operations to solve the following problems

1. check whether the number `12` is an integer or not
2. divide `100` by `12` and check whether the number is `float` or not
3. suppose we have following lists:

   ``` python
   x = [1,2,3,4,5]
   y = [1,2,3,4,5]
   z = x
   ```

    1. Is `x` identical to `y`?
    2. Is `x` identical to `z`?

   _Solve problems programmatically and write the reasons why they are or are not identical with each other._
4. Suppose there are following animals in the zoo:

   `elephant`, `tiger`, `zebra`, `lion`, `wolf`
    1. Check programmatically whether `lion` is in the zoo or not.
    2. Check programmatically whether `horse` is in the zoo or not.
5. Create a list of first 7 prime numbers and check whether 9 is a prime number or not using membership operation.

## Quiz Q0211

Use bitwise operations to perform the following:

1. Check the final value when `5` is performed bitwise AND with `7`
2. Check the final value when `5` is performed bitwise OR with `2`
3. `y = 10 * 2`. Solve the same problem using bitwise shift operation.
4. Multiply and divide an integer by 4 using bitwise shift operations.
