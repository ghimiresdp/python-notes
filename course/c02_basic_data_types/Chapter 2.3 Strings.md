- **created by**: Sudip Ghimire
- **URL**: [https://www.sudipghimire.com.np](https://www.sudipghimire.com.np)
- **GitHub**: [https://github.com/ghimiresdp](https://github.com/ghimiresdp)

[go to course contents](https://github.com/ghimiresdp/python-level1/)
-----------------------
# Chapter 2.3 Strings
**Table of Contents**
- [Chapter 2.3 Strings](#chapter-23-strings)
    - [Introduction to Strings](#introduction-to-strings)
    - [Escape Characters](#escape-characters)
    - [String Concatenation](#string-concatenation)
    - [Finding out the length of the string](#finding-out-the-length-of-the-string)
    - [Capitalization, Upper Case and Lower Case conversion](#capitalization-upper-case-and-lower-case-conversion)

## Introduction to Strings

Strings are iterable set of characters enclosed within single-quotation marks `''` or double-quotation marks`""`. Multiline strings are enclosed with triple single-quotation marks `'''` or triple double-quotation marks `"""`. Strings are generally immutable, but when we try to change the value of string to a variable, a completely new object is created and assigned to the variable. With strings created with single quotes `''`, we can use double quotes`""` inside it without any escape characters. Some of the examples of strings are as follows:

```python
name = 'John Doe'              # String with single quotation marks
full_name = "I am John Doe"    # String with double quotation marks

desc = 'He said, "I am John Doe".'

# Multi line strings
essay = '''Strings are iterable set of characters enclosed within
single-quotation marks or double-quotation marks.
'''
```

If we want to have single quote inside a single quoted string and a double quote inside a double quoted string then, we need to escape the characters with backslash `\`.

## Escape Characters

Escape character is a character, that invokes the alternative interpretation of some of the characters that we can not directly type inside the string. For example if we want to add a new line inside a string of python, pressing the <kbd>Enter</kbd> key for new line tries to terminate the statement so we need to type `\n` as the escape character for <kbd>Enter</kbd>. Some of the escape characters and their meanings are as follows:

| Escape Character | Expected Behavior     |
|:----------------:| --------------------- |
| `\t`             | Tabs                  |
| `\n`             | New Line              |
| `\"`             | Double quotation Mark |
| `\'`             | Single Quotation Mark |
| `\\`             | Backslash             |
| `\a`             | Ascii Bell            |
| `\b`             | Backspace             |
| `\r`             | Carriage Return       |
| `\v`             | Vertical Tab          |

for more detail about escape characters, please see https://docs.python.org

Examples:

```python
content_1 = 'This is the first line.\nThis is the second line.'
print(content_1)

content_2 = 'John said, "I\'m a good student".'
print(content_2)
```

Output:

```
This is the first line.
This is the second line.
John said, "I'm a good student".
```

## String Concatenation

Concatenation is the process of merging 2 or more strings. We generally use `+` operator to merge 2 strings.

```python
first_name = 'John'
last_name = 'Lennon'
full_name = first_name + last_name    # 'JohnLennon'
```

## Finding out the length of the string

We can find out the length of the string by 2 different ways which are as follows:

- **`str.__len__()`** method

- **`len()`** function

  ```python
  paragraph = 'A quick brown fox jumps over the lazy dog.'
  print(paragraph.__len__())    # 42
  print(len(paragraph))         # 42
  ```

## Capitalization, Upper Case and Lower Case conversion

python has plenty of options in changing the case of the string. Capitalization is the process of capitalizing the first character of the string. Upper and Lower case conversion just converts the string to its respective cases.

```python
'john'.capitalize()    # John
'john'.upper()         # JOHN
'JOHN'.lower()         # john

text = 'A quick brown fox jumps over the lazy dog.'
print(text.upper())    # A QUICK BROWN FOX JUMPS OVER THE LAZY DOG
```
