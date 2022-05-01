# REGEX Special characters in Regex

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

`\A` Matches only at the start of the string
`\b` Matches the empty string but only ar the beginning or the end of the string.
`B` Matches the empty string but only when it is not at the beginning or the end of a word
`\d` Matches a number from 0-9
`\D` Matches a character except a number from 0-9
`\s` Matches white space character such as space or tab
`\S` Matches a character except white space characters
`\w` Matches a character that contains alphanumeric character or `_` character
`\W` Matches any character except alphanumeric or `_` character
`\Z` Matches only at the end of the string


