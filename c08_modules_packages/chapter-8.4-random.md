# Chapter 8.4. The `random` Module

**Table Of Contents**:

- [Chapter 8.4. The `random` Module](#chapter-84-the-random-module)
  - [Usage](#usage)
    - [Printing out a random number from a range 1 to 6](#printing-out-a-random-number-from-a-range-1-to-6)
    - [Printing out 10 random numbers from a range 1 to 6](#printing-out-10-random-numbers-from-a-range-1-to-6)
    - [Printing out a random character from a string](#printing-out-a-random-character-from-a-string)
    - [Printing out 5 random characters as a list from a string](#printing-out-5-random-characters-as-a-list-from-a-string)
    - [Printing out a random password string with 8 characters](#printing-out-a-random-password-string-with-8-characters)

Reference: <https://docs.python.org/3/library/random.html>

- `random` module implements pseudo-random generators for various distributions.

**Some of the functions are as follows:**

- `random.seed()`

  It initializes the random number generator.

- `random.randrange()`

  It accepts 3 parameters `start`, `stop`, and `step` which is similar to `range()` function. It returns the random from the eligible numbers from the range function.

- `random.randint()`

  It is similar to `randrange()` method but the `stop` number is inclusive

- `random.choice()`

  It chooses a character from the string provided.

- `random.choices()`

  It chooses `k` number of characters as a list from the string provided.

## Usage

### Printing out a random number from a range 1 to 6

```python
import random

print(random.randint(1,6))
```

### Printing out 10 random numbers from a range 1 to 6

```python
import random

for _ in range(10):
    print(random.randint(1,6))
```

### Printing out a random character from a string

```python
import random

options = "12345ABCDEabcde"
print(random.choice(options))
```

### Printing out 5 random characters as a list from a string

```python
import random

options = "12345ABCDEabcde"
print(random.choices(options, k=5))
```

### Printing out a random password string with 8 characters

```python
import random

options = "12345ABCDEabcde"
print(''.join(random.choices(options, k=8)))
```
