- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp

**Table of Contents**
- [`Datetime` Module](#datetime-module)
  - [`datetime` Constants](#datetime-constants)
  - [`datetime` Data types](#datetime-data-types)
    - [1. class `datetime.date`](#1-class-datetimedate)
    - [2. class `datetime.time`](#2-class-datetimetime)
    - [3. class `datetime.datetime`](#3-class-datetimedatetime)
    - [4. class `datetime.timedelta`](#4-class-datetimetimedelta)
    - [5. class `datetime.tzinfo`](#5-class-datetimetzinfo)
    - [6. class `datetime.timezone`](#6-class-datetimetimezone)
  - [Datetime Operations](#datetime-operations)
    - [Adding `timedelta` to the`datetime` instance.](#adding-timedelta-to-thedatetime-instance)
    - [Subtracting two `datetime` instances](#subtracting-two-datetime-instances)
  - [Parsing and formatting the datetime](#parsing-and-formatting-the-datetime)
    - [The `strftime()` method](#the-strftime-method)
    - [The `strptime()` method](#the-strptime-method)

# `Datetime` Module

Reference: https://docs.python.org/3/library/datetime.html


The `datetime` module supplies different classes for manipulating date and time instances. We can perform different
mathematical operations

## `datetime` Constants

The  `datetime` module exports following constants.

- `datetime.MINYEAR`: 1
- `datetime.MAXYEAR`: 9999


## `datetime` Data types

The `datetime` module exports following data types:

### 1. class `datetime.date`

The `datetime.date` class can create a `date` object that accepts 3 parameters, i.e. `year`, `month`, and `day` as
numbers to instantiate the `date` object.

**initializing `date` object**
```python
from datetime import date

date_1 = date(1999, 12, 31)  # 1999-12-31
date_2 = date(year=1999, month=12, day=31)
```

### 2. class `datetime.time`
The `datetime.time` class accepts `hour`, `minute`, `second`, `microsecond`, `tzinfo` (optional) parameters that has
default values of 0. the `datetime.time` class creates `time` object.

**initializing `time` object**

```python
from datetime import time

time1 = time(hour=5)    # 05:00:00
time2 = time(hour=5, minute=50) # 05:50:00
time3 = time(hour=5, minute=50, second=30)  # 05:50:30
time4 = time(hour=5, minute=50, second=30, microsecond=100)  # 05:50:30.000100
```

### 3. class `datetime.datetime`
The class `datetime.datetime` is a combination of `datetime.date` and `datetime.time` classes. It can accept all
attributes of both `date`, and `time` objects. the parameters of `datetime` class are as follows:

`datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])`

The `year`, `month` and `day` arguments are required. `tzinfo` may be None, or an instance of a tzinfo subclass. The remaining
arguments may be ints and has default value `0`.

**initializing `datetime` object**
```python
from datetime import datetime

datetime_1 = datetime(1999, 12,31, 23,59,59, 100)   # 1999-12-31 23:59:59.000100
```

### 4. class `datetime.timedelta`
A `datetime.timedelta` class is a duration of time that expresses the difference between two `date`, `time`, or
`datetime` instances to microsecond resolution

**initializing the `timedelta` object
```python
from datetime import timedelta

d1 = timedelta(hours= 10)
d2 = timedelta(days=30, hours=20, minutes=50, seconds=30)   # 30 days, 20:50:30
```

### 5. class `datetime.tzinfo`
`tzinfo` is an abstract base class for time zone information objects. these are used by the datetime and time class to
provide ta customizable notion of time adjustment.


### 6. class `datetime.timezone`
 `timezone` class is a class that implements `tzinfo` abstract base class that has a fixed offset from the UTC.

```python
from datetime import timezone, timedelta
tz1 = timezone(offset=timedelta(hours=5, minutes=45))
```



## Datetime Operations

### Adding `timedelta` to the`datetime` instance.

We can add `timedelta` value to `date` or `datetime` instance to get the new `date` or `datetime`.

```python
from datetime import date, datetime, timedelta

date_1 = date(1999, 12, 31)
date_2 = date_1 + timedelta(days=5)  # 2000-01-05

datetime_1 = datetime(1999, 12, 31, 12, 30, 50)

datetime_2 = datetime_1 + timedelta(days=5, hours=10)  # 2000-01-05 22:30:50
```

**Note**: _we cannot add two `date` or `datetime` instances to get a new `date` or `datetime` instance._

### Subtracting two `datetime` instances

We can subtract one `date` or `datetime` instance from another `date` or `datetime` instance to get the time difference
as `timedelta` instance.

```python
from datetime import date, datetime
date_1 = date(1999, 12, 31)
date_2 = date(1999, 10, 15)
diff_1 = date_1 - date_2	# 77 days, 0:00:00

datetime_1 = datetime(1999, 12, 31, 12, 30, 50)
datetime_2 = datetime(1999, 10, 15, 19, 45, 21)
diff_2 = datetime_1 - datetime_2	# 76 days, 16:45:29
```

**Note**: _Subtracting two `date` or `datetime` instances always give `timedelta` instance._


## Parsing and formatting the datetime
- We can parse the date from the string with the `strptime()` method and format the date string with the `strftime()` method.

### The `strftime()` method
The `strftime()` method takes format string and returns the formatted date string.
```python
today = date.today()
print(today.strftime("%b %d, %Y"))   # Mar 10, 2022
```

### The `strptime()` method
the `strptime()` method takes 2 parameters `datetime string` and the format string to parse the datetime. It returns the `datetime` object.

```python
date_str = "2000/12/31"
date_time = datetime.strptime(date_str, "%Y/%m/%d")
```

Please refer to https://docs.python.org/3/library/datetime.html for more information about the datetime module and their operations.
