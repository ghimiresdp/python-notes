> - **created by**: Sudip Ghimire
> - **URL**: https://www.sudipghimire.com.np
> - **GitHub**: https://github.com/ghimiresdp
>
> [go to course contents](https://github.com/ghimiresdp/python-notes/)

**Table of Contents**


# 13.3. The `filter()` function

https://docs.python.org/3/library/functions.html#filter

A `filter()` function is a generator function that filters an iterable by specified condition. A filter function takes

```py
def is_even(num):
    return num%2==0

list_1 = [1,2,3,4,5,6,7,8,9,10]

list_2 = filter(is_even, list_1)

print(list(list_2))
```
