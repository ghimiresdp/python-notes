- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp

**Table of Contents**
- [14.3. The `re` module](#143-the-re-module)
  - [`re.compile()` function](#recompile-function)
  - [`re.search()` function](#research-function)
  - [`re.match()` function](#rematch-function)
  - [`re.findall()` function](#refindall-function)
  - [`re.split()` function](#resplit-function)
  - [`re.sub()` function](#resub-function)

# 14.3. The `re` module

This chapter covers some examples of the regular expression using `re` module. If you're not reviewed
regular expressions and regex special characters, please review them first.

- [Chapter 14.1 Regular Expressions](chapter%2014.1%20regular%20expressions.md)
- [Chapter 14.2 Regex Special Characters](chapter%2014.2%20regex%20special%20characters.md)

or you can look at the official documentation from https://docs.python.org/3/library/re.html.


The `re` module contains several functions that helps finding out, compiling and matching regular expressions. Some of the functions are as follows:

## `re.compile()` function

The `re.compile()` function compiles the regular expression from the regular string to a regular expression object. It takes 2 arguments:
- `pattern`: a regular expression as a string
- `flags`: a value that can be specified to modify default behavior. _defaults to 0_
  Some example of flags are as follows:
    - `re.A` or `re.ASCII`: Matches only ASCII matching instead of unicode matching.
    - `re.I` or `re.IGNORECASE`: Expressions like `[A-Z]` also matches lowercase when this flag is specified
    - `re.M` or `re.MULTILINE`: The pattern character `^` also matches the beginning of each line.
    - `re.X` or `re.VERBOSE`: This flag allows us to write regex in a more readable way
    - `re.DEBUG`: Displays debug information
- The function returns a `re.Pattern` object which can then be used to match, search, or find all occurrences with that pattern.

**Example 1**: A regular expression that extracts the name of a country that starts with A and ends with a
```python
import re
countries = ['USA', 'Japan', 'Angola', 'China', 'Algeria', 'Nepal', 'Argentina', 'Albania']

pattern = re.compile(r'^A\w*a$')

```
The above pattern when matched with the list of countries should give matches for _Angola_, _Algeria_, _Argentina_ and _Albania_

```python
countries = ['USA', 'Japan', 'Angola', 'China', 'Algeria', 'Nepal', 'Argentina', 'Albania']

# a word that starts with A and ends with a
pattern = re.compile(r'^A\w*a$')

for country in countries:
    print(pattern.match(country))

# Output
"""
None
None
<re.Match object; span=(0, 6), match='Angola'>
None
<re.Match object; span=(0, 7), match='Algeria'>
None
<re.Match object; span=(0, 9), match='Argentina'>
<re.Match object; span=(0, 7), match='Albania'>
"""
```

**Example 2**: compile a regular expression that can match hexadecimal strings:
```py
import re

strings = ["0xaa", 'FA04', 'Ak45','As40', '0x5h', '0x56']

pat = re.compile(r'^(0x)?[0-9A-Fa-f]+$')

for st in strings:
    print(pat.match(st))

# output
"""
<re.Match object; span=(0, 4), match='0xaa'>
<re.Match object; span=(0, 4), match='FA04'>
None
None
None
<re.Match object; span=(0, 4), match='0x56'>
"""
```
Explanation: Here the pattern looks for optional `0x` character which can be represented to display hexadecimal digit. and the pattern should contain at least 1 digit from 0-9 or a-f in any case.

## `re.search()` function

The `re.search()` function starts scanning the string for the first match of the regex and returns a corresponding match object.
It returns `None` if there is no match throughout the string.

**Note**: _It does not return multiple match objects if the string contains multiple matches._

**Example 3**:search for the pattern which contains _mail_ or _email_.

```py
import re

text = "Dear sir, I've emailed you last week regarding the assignment. I've also sent you another mail specifying the next assignment."

results = re.search(r'e?mail(ed)?', text)
print(results)

# Output
# <re.Match object; span=(15, 22), match='emailed'>

```

## `re.match()` function
If zero or more characters at the beginning of the string match the regular expression pattern, it returns a corresponding match object.
It returns`None` if there is no match for the regex. The `re.match()` function takes 3 parameters which are as follows:

- _pattern_: the regex pattern
- _string_: the string in which we try to find the match
- _flag_: the flag to change the default behavior of the regex. ([similar to `re.compile()` function](#recompile-function))

**Example 4**: Match if the first word contains a letter `e` in the second position.
```py
import re

text = 'Dear sir'
print(re.match(r'[a-z]e\w+', text, re.I))
"""
# output
<re.Match object; span=(0, 4), match='Dear'>
"""
```

**Note**: _It does not return any matches if it can't match at the beginning of the string. If we want to locate a match anywhere in the string then we can use [the `re.search()` function](#research-function) instead._

## `re.findall()` function
## `re.split()` function
## `re.sub()` function
