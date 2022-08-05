- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

[go to course contents](https://github.com/ghimiresdp/python-level1/)
-----------------------

# Chapter 4. Decision Making

**Table of Contents**
- [Chapter 4. Decision Making](#chapter-4-decision-making)
    - [Introduction](#introduction)
    - [The `if` condition](#the-if-condition)
    - [The `if else` condition](#the-if-else-condition)
    - [The `if elif else` condition](#the-if-elif-else-condition)
    - [Ternary operators](#ternary-operators)
    - [Nested Conditions](#nested-conditions)

## Introduction

Decision Making (Also known as conditional branching) is the process of running
certain part of code whenever the condition satisfies. For example, If we want
to allow the player if he/she is 18 years or older only then, we need to
create condition that handles the game with respect to the age.

We use `if`, `elif`, and `else` conditions to perform conditional branching.

## The `if` condition
- It is written with `if` keyword
- code blocks that should run whenever the condition matches are indented.
- We need to un-indent the code block to represent the end of a code block.

Syntax:
```
if <contition>:
    statements that need to run when the condition fulfills
    ...

end of the code block
```

**Example 1**: Condition is satisfied

```python
a = 20
b = 25
if a < b:
    print(f'{a} is less than {b}')
print('I am outside of the code block')

'''
out:
20 is less than  25
I am outside of the code block
'''
```

**Example 2**: Condition is not satisfied

```python
a = 20
b = 25
if a > b:
    print(f'{a} is greater than {b}')   # this code block does not run
print('I am outside of the code block')

'''
out:
I am outside of the code block
'''
```

## The `if else` condition

The `if else` condition is similar to the `if` condition but has another code
block that runs when the condition is not satisfied.

**Syntax**
```
if <condition>:
    code block that runs only when condition is satisfied
else:
    code block that runs if the condition is not satisfied
```

**Example**
```python
x = 5
if x % 2 == 0:
    # this code block runs only when x is assigned even numbers
    print(f'{x} is even number')
else:
    # this code block runs only when x is assigned odd numbers
    print(f'{x} is odd number')
```

## The `if elif else` condition

The `if elif else` condition adds more flexibility to branching providing more than one conditions.

**Syntax**
```
if <condition 1>:
    code block that runs only when condition satisfies
elif <condition 2>:
    code block that runs if the condition 1 satisfies and condition 2 satisfies
...
elif <condition n>:
    ...
else:
    code block that runs only if all of above condition does not satisfy
```

**example**
```python
num = 12

if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")

elif num % 2 == 0:
    print("Divisible by only 2")

elif num % 3 == 0:
    print("Divisible by only 3")

else:
    print("Not divisible by both 2 and 3")
```

**Note**:
In case of `if elif` conditions, if the first condition satisfies, it
never goes to check another condition so we need to make sure we're using it
properly to get the expected output

## Ternary operators

Ternary operators are also known as single statement conditional branching and
are used whenever we have conditions that has only one statement or assignment
operation.

Example:

```python
if x < 7:
    size = 'small'
elif x >= 7 and x < 1:
    size = 'medium'
else:
    size = 'large'
```

The Above statement can be converted into single statement conditional branching
using the following code:

```python
size = 'small' if x < 7 else ('medium' if (7 <= x < 10) else 'large')
```


## Nested Conditions

Nested conditions are conditions that exist within another condition.

```python
number = 20
if number < 10:
    if number % 2 == 0:
        print('The number is even and less than 10')
    else:
        print('The number is odd and less than 10')
else:
    if number % 3 == 0:
        print('The number is divisible by 3 and greater than 10')
    else:
        print('The number is not divisible by 3 and greater than 10')

```
