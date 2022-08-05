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
is true. It repeatedly tests the expression and executes
statements within the code block until the condition fails to satisfy.

To skip statements for one time, we use `continue` statement and to terminate the execution in special conditions, we use the `break` statement.

## A generic while loop

The `while` loop is used for iterating until the condition fails to satisfy.
Generally, the `while` loop contains:
- A _condition_ to check whether it satisfies to run further
- A _statement_ that runs when it satisfied
- An _update_ statement that is capable of dynamically changing the state that
  eventually changes the condition

```python
while <condition>:
    # statements that should executed while condition satisfies
    <update statement>
```

**Example**: print the value from 1 upto 10
```python
x = 1
while x <=10:
    print('The current value of x is: ', x)
    x += 1
print('The loop is completed')
```

**Output**:
```
The current value of x is:  1
The current value of x is:  2
The current value of x is:  3
The current value of x is:  4
The current value of x is:  5
The current value of x is:  6
The current value of x is:  7
The current value of x is:  8
The current value of x is:  9
The current value of x is:  10
The loop is completed
```

**Example 2**:

Write a program that inputs names of students until the user enters `exit` and
display the list at the end.

```python
name_list = []
name = ''
while name.lower() != 'exit':
    name = input('Enter the name: ')
    name_list.append(name)
print(name_list[:-1])
```


**Output**
```
Enter the name: ABC
Enter the name: DEF
Enter the name: GHI
Enter the name: JKL
Enter the name: exit

['ABC', 'DEF', 'GHI', 'JKL']
```

## While else
**Syntax:**
```python
while <condition>:
    statements
else:
    alternative statements when while condition is not fulfilled
```

**Example:**

```python
x = 1
while x <= 10:
    print('The current value of x is: ', x)
    x += 1
else:
    print('Now the value is greater than 10')
```

**Output**
```
The current value of x is:  1
The current value of x is:  2
The current value of x is:  3
The current value of x is:  4
The current value of x is:  5
The current value of x is:  6
The current value of x is:  7
The current value of x is:  8
The current value of x is:  9
The current value of x is:  10
Now the value is greater than 10
```

## The `break` and the `continue` Statement

To skip execution in some conditions, we can use `continue` statement. The
`break` statement breakes the execution out of the loop. These statements are
useful when we have infinite number of iterations and want to break on some
conditions.

**Syntax:**
```python
while <condition>:
    statements

    if <special condition>:
        break

    if <some condition>:
        continue
```

**Example 1:**

```python
x = 0
while x < 100:  # this indicates x can loop until it is 100
    x += 1
    if x % 3 == 0:
        continue    # this statement skips for all multiples of x
    if x > 10:
        break   # This statement breaks the loop whenever the value of x > 10
    print('The current value of x is: ', x)

```

**Output:**
```
The current value of x is:  1
The current value of x is:  2
The current value of x is:  4
The current value of x is:  5
The current value of x is:  7
The current value of x is:  8
The current value of x is:  10
```


**Example 2:**
Write a program that displays all words entered by the user.
- The program should sensor slightly offensive words and skip execution for one time
- The program should immediately exit when highly offensive words are used
- Check the word if it is palindrome if it is not offensive.

```python
offensive = ['dull', 'ugly', 'short',]
highly_offensive = ['dog', 'shit', 'damn', 'beat',]

while True:
    word = input('\nEnter The word: ').lower()
    if word in offensive:
        print(f'The word {word[0]}{"*" * (len(word) - 1)} is offensive, so skipping execution...')
        continue
    if word in highly_offensive:
        print("You used Highly offensive word, Good Bye!!")
        break
    if word == word[::-1]:
        print('The word is palindrome')
    else:
        print('The word is not palindrome')

```

**Output:**
```
Enter The word: human
The word is not palindrome

Enter The word: rotator
The word is palindrome

Enter The word: ugly
The word u*** is offensive, so skipping execution...

Enter The word: short
The word s**** is offensive, so skipping execution..
.
Enter The word: dog
You used Highly offensive word, Good Bye!!
```
