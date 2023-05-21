- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp

**Table of Contents**
- [14.2. REGEX Special characters in Regex](#142-regex-special-characters-in-regex)
  - [Special Characters](#special-characters)
  - [Escape Sequences in a regular expression](#escape-sequences-in-a-regular-expression)
  - [Set of characters in regex](#set-of-characters-in-regex)
# 14.2. REGEX Special characters in Regex

There are various special characters in regex which are listed as follows:

## Special Characters

|   SN | symbol           | Description                                                             |
| ---: | ---------------- | ----------------------------------------------------------------------- |
|    1 | `.`              | Matches any character except newline character                          |
|    2 | `^`              | Matches starting of the string                                          |
|    3 | `$`              | Matches end of the string                                               |
|    4 | `*`              | Matches `0` or more occurrences                                         |
|    5 | `+`              | Matches `1` or more occurrences                                         |
|    6 | `?`              | Matches 0 ir 1 occurrences                                              |
|    7 | `{m}`            | Matches exactly `m` number of occurrences                               |
|    8 | `{m,n}`          | Matches `m` to `n` occurrences                                          |
|    9 | `{m,n}?`         | Tries to match as few occurrences as possible but with in range `{m,n}` |
|   10 | `*?`, `+?`, `??` | Tries to match as few occurrences qualified by `*`, `+`, and `?`        |
|   11 | `\`              | Escapes the regular character or special character                      |
|   12 | `[]`             | Matches any character that is written within the brackets               |
|   13 | `A\|B`           | Matches `A` or `B`                                                      |
|   14 | `(...)`          | Matches whatever regular expression is inside parenthesis               |


## Escape Sequences in a regular expression

Regular expression escape sequences not only escapes regular characters but special characters too.
for example if we want to include a character `*` in regular expression, it has it's own meaning which means it needs to be escaped. by writing `\*`
 |   SN | Symbol | Description                                                                            |
 | ---: | ------ | -------------------------------------------------------------------------------------- |
 |    1 | `\A`   | Matches only at the start of the string                                                |
 |    2 | `\b`   | Matches the empty string but only ar the beginning or the end of the string.           |
 |    3 | `B`    | Matches the empty string but only when it is not at the beginning or the end of a word |
 |    4 | `\d`   | Matches a number from 0-9                                                              |
 |    5 | `\D`   | Matches a character except a number from 0-9                                           |
 |    6 | `\s`   | Matches white space character such as space or tab                                     |
 |    7 | `\S`   | Matches a character except white space characters                                      |
 |    8 | `\w`   | Matches a character that contains alphanumeric character or `_` character              |
 |    9 | `\W`   | Matches any character except alphanumeric or `_` character                             |
 |   10 | `\Z`   | Matches only at the end of the string                                                  |

## Set of characters in regex

A set of characters in regex are denoted inside a pair of square brackets [].
Unlike special characters in regular regex, special characters (such as `*`, `+`, etc) inside
large brackets has no meaning.

**some of the regex set matches are as follows:**

|   SN | Symbol        | Description                                                                         |
| ---: | ------------- | ----------------------------------------------------------------------------------- |
|    1 | `[abc]`       | matches either of `a`, `b` or `c`.                                                  |
|    2 | `[a-m]`       | matches either of character from `a` to `m`                                         |
|    3 | `[a-m0-5]`    | matches either of character from `a` to `m` followed by number from `0` to `5`      |
|    4 | `[0-9A-Fa-f]` | matches any hexadecimal character from `0-9` and `a-f` or `A-F`                     |
|    5 | `[^abc]`      | matches either of character except `abc`                                            |
|    6 | `[0123]`      | matches either of `0`, `1`, `2`, or `3`                                             |
|    7 | `[ab][12]`    | matches either of `a1`, `a2`, `b1`, or `b2`                                         |
|    8 | `[+*]`        | matches either of `+` or  `*` characters (but no matches for number of occurrences) |


We can also find the number of occurrences of set of characters by specifying `*`, `+` or `?` after brackets.

**For Example:**

- `[0-9A-Fa-f]+` matches any number of occurrences that matches `[0-9A-Fa-f]`. Example: `0`, `1`, `1A`, `ff0c`, etc.
- `[\d]{4}` matches exactly 4 numeric characters from the string.
