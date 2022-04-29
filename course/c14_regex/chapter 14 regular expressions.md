- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp

**Table of Contents**

# Chapter 14 Introduction to Regular Expressions

**res**: https://docs.python.org/3/library/re.html

Python has a standard library for regular expressions called `re` module. The `re` module provides us regular expression matching operations.

Both _Unicode Strings_ and _Byte Strings_ can be searched using regular expressions in python however both cannot be mixed.

Regular Expressions contain even wider range of escape characters to represent different patterns inside strings.


Let us suppose we have the sentence:

```python
str_1 = 'Regular expressions are better pattern matchers.'
```

**Example 1:**
If we want to match all `er` from the above string like shown below:

    > Regular expressions are bett`er` patt`er`n match`er`s.

    We can match the regular expression by specyfing regex string as: `r'er'`


**Example 2:**
If we want to match all `er` and `ar` from the above string like shown below:

> Regul`ar` expressions `ar`e bett`er` patt`er`n match`er`s.

We can match the regular expression by specifying regex string as: `r'[ae]r'`


**Example 3:**
If we want to match all the occurence that start with `J` and end with `n` from the following expression:

```python
str_1 = 'John, Jane, Jennifer, Joan, Jon, Adam, Eve'
```

We can match the regular expression by specifying regex string as: `r'J\w*n'` which results in matching the following:

> `John`, `Jan`e, `Jenn`ifer, `Joan`, `Jon`, Adam, Eve'

The example code snippet would be:

```py
import re
str_1 = 'John, Jane, Jennifer, Joan, Jon, Adam, Eve'
print(re.findall(r'J\w*n', str_1))

# ['John', 'Jan', 'Jenn', 'Joan', 'Jon']
```
