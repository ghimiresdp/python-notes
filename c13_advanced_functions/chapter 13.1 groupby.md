- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp

# 13.1. The `groupby()` Function


The `groupby()` function is a function that returns consecutive keys and groups from the iterable.

The `groupby()` generates an iterator that has key and value pair in which key is the value to be grouped by and value is the iterator again which contains grouped value.
Source: https://docs.python.org/3/library/itertools.html#itertools.groupby

**Example 1**
```python
# example 1
animals = ['Bear', 'Donkey', 'Cat', 'Dog', 'Camel', 'Elephant']
animals = sorted(animals)
values = groupby(animals, lambda x: x[0])
grouped = {k: list(v) for k, v in values}
print(grouped)
```

Output
```
{'B': ['Bear'], 'C': ['Camel', 'Cat'], 'D': ['Dog', 'Donkey'], 'E': ['Elephant']}
```


