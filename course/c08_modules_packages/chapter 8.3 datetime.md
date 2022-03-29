- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp

# `Datetime` Library

Reference: https://docs.python.org/3/library/datetime.html


A datetime library is the python standard library that supplies classes for manipulating dates and times.

Basic classes that are used in daily life:

- `datetime.date`
- `datetime.time`
- `datetime.datetime`
- `datetime.timedelta`

## Importing package and components


```python
# importing the whole package
import datetime

# importing individual components
from datetime import date, datetime, timedelta
```

# Initializing the `date` class

- We can initialize the `date` class by arguments in order `year`, `month`, and `day`.
- We can also initialize the class by named argument in any order.

```python
from datetime import date

date_1 = date(1999, 12,31)
date_2 = date(day=20, month=10, year=1990)

date_3 = date.today()   # it gives the current system date
```

# initializing the `datetime` class
- We can initialize the `datetime` class by arguments in order `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond`, `tzinfo` where `year`, `month` and `day` are required.
- We can also initialize the class by named argument in any order.

```python
from datetime import datetime

time_1 = datetime(1999, 12, 31, 23, 59, 59, 999999)
time_2 = datetime(year=1990, month=1, day=31, hour=23, minute=58, second=59, microsecond=999900)

time_3 = datetime.now() # it gives the current system date and time

```

# Initializing the `timedelta` class

- `timedelta` class is the class that is used to store the amount of time rather than current or previous time.
- example of `timedelta` is 10 minutes, or 1 year
- we can initialize the `timedelta` class by providine any or all of the named arguments `days`, `seconds`, `microseconds`, `milliseconds`, `minutes`, `hours` and `weeks`.

```python
from datetime import timedelta

# the value is 5 minutes and 30 seconds
td_1 = timedelta(minutes = 5, seconds=30)
```


# datetime operations

## addition
We can add `timedelta` to a `date` or `time` or `datetime` or a `timedelta` instance but adding two `datetime` or `date` instances is not allwoed.

```python
date_next_week = date.today() + timedelta(days=7)

time_next_hr = datetime.now() + timedelta(hours=1)

```

## Subtraction
We can subtract two `date` or `datetime` instances to get the difference as `timedelta` object.

```python
today = date.today()
new_year = date(2022, 1, 1)

difference = today - new_year   # the difference is timedelta instance

```

# Parsing and formatting the datetime
- We can parse the date from the string with the `strptime()` method and format the date string with the `strftime()` method.

## The `strftime()` method
The `strftime()` method takes format string and returns the formatted date string.
```python
today = date.today()
print(today.strftime("%b %d, %Y"))   # Mar 10, 2022
```

## The `strptime()` method
the `strptime()` method takes 2 parameters `datetime string` and the format string to parse the datetime. It returns the `datetime` object.

```python
date_str = "2000/12/31"
date_time = datetime.strptime(date_str, "%Y/%m/%d")
```

Please refer to https://docs.python.org/3/library/datetime.html for more information about the datetime module and their operations.
