- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **GitHub**: https://github.com/ghimiresdp

# Chapter 5.1: While Loops

**Table of Contents:**
- [Chapter 5.1: While Loops](#chapter-51-while-loops)
    - [Introduction to while loop](#introduction-to-while-loop)
    - [A generic while loop](#a-generic-while-loop)
    - [While else](#while-else)
    - [The `break` and the `continue` Statement](#the-break-and-the-continue-statement)

## Introduction to while loop

The `while` statement is used for repeated execution as long as the expression
is true. This repeatedly tests the expression and if it is true, it executes
statements within the code block and for the next iteration, it again checks
the condition.

To terminate the execution in special conditions, we use the `break` statement.

## A generic while loop


```python
while <condition>:
    statements
```

## While else
**Syntax:**
```python
while <condition>:
    statements
else:
    alternative statements
```


## The `break` and the `continue` Statement

**Syntax:**
```python
while <condition>:
    statements

    if <special condition>:
        break

    if <some condition>:
        continue
```
