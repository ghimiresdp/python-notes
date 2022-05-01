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
|   12 | `[abc]`          | Matches either of `a`, `b` or `c`                                       |
|   12 | `[a-m]`          | Matches any characters within `a` to `m`                                |
|   13 | `A\|B`           | Matches `A` or `B`                                                      |
|   14 | `(...)`          | Matches whatever regular expression is inside parenthesis               |
