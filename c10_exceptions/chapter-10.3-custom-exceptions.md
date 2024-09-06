# Creating custom Exceptions

We can create a new `Exception` by inheriting the `BaseException` class. The
following is an example of a CustomException:

```py
class MyCustomException(Exception):
    pass
```

## Example1: AgeError

We can create a custom age error that can raise the exception if a user enters
the invalid range of an age of a person.

```py
class AgeError(Exception):
    min_age = 0
    max_age = 100

    def __init__(self, age, *args):
        super().__init__(*args)
        self.age = age

    def __str__(self):
        return f'The age {self.age} is not in between {self.min_age} and {self.max_age}'
```

## Example2: `LengthError`

The example below explains how a custom exception can be raised using the
object-oriented oriented approach:

```py
class LengthError(Exception):
    def __init__(self, value: int,  *args: object) -> None:
        self.value = value
        super().__init__(*args)

    def __str__(self):
        return f'The length {self.value} is not possible'


class Length:
    def __init__(self, value):
        if value < 0:
            raise LengthError(value)
        self.value = value


l1 = Length(5)
l2 = Length(-5)     # LengthError: The length -5 is not possible
```
