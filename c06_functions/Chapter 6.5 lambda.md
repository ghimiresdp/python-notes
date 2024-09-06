# Chapter 6.5: Lambda Expressions

**Table of Contents**:

- [Chapter 6.5: Lambda Expressions](#chapter-65-lambda-expressions)
  - [Introduction](#introduction)
  - [Lambda function with Zero arguments](#lambda-function-with-zero-arguments)
  - [Ternary operators on lambda functions](#ternary-operators-on-lambda-functions)

## Introduction

In python Lambda functions or lambda expressions are single line expressions
with no name that can have any number of arguments. Lambda functions are also
called as anonymous functions or one-liner functions. Lambdas are useful when
we have to do small repetitive tasks.

**Basic Syntax:**

```python
value = lambda arg_1, arg_2, ..., arg_n : return_expression
```

here, everything separated with comma before `:` are arguments and the
expression after `:` is used as the return value or expression. Lambda
expression do not expect `return` keyword however whatever expression is
written after the colon `:`, will be treated as return statement.

**Example 1:** A lambda to add 2 values

```python
add_num = lambda a,b: a+b

print(add_num(5, 6))  # 11
```

## Lambda function with Zero arguments

We can also create a lambda expression with zero arguments. To create a lambda
with zero arguments, we just use `lambda` keyword before a colon `:`.

**Example 2:** Lambda to print Hello World

```python
hello_world = lambda: "Hello World"

print(hello_world())    # Hello World
```

## Ternary operators on lambda functions

```python
odd_even = lambda num: 'Even' if num % 2 == 0 else 'Odd

print(odd_even(14))     # Even
```
