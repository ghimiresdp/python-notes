- **created by**: Sudip Ghimire
- **URL**: https://www.sudipghimire.com.np
- **Github**: https://github.com/ghimiresdp

**Table of Contents**
- [13.2. The `sorted()` Function](#132-the-sorted-function)
  - [Sorting the list in an ascending order](#sorting-the-list-in-an-ascending-order)
  - [Sorting the list in a descending order](#sorting-the-list-in-a-descending-order)
  - [Complex Sorting with the `sorted()` function](#complex-sorting-with-the-sorted-function)
    - [a `key` parameter in `sorted()` function](#a-key-parameter-in-sorted-function)
# 13.2. The `sorted()` Function

https://docs.python.org/3.9/howto/sorting.html

Although there's a `list.sort()` method that modifies the list in place, we need to return the sorted list without modifying the original list. for that purpose, we can use `sorted()` function that builds a new sorted list from an iterable


## Sorting the list in an ascending order
Sorting the list in an ascending order is done by just passing the list as an argument in the `sorted()` function.

```py
print(sorted([1, 4, 7, 2, 9, 5, 3]))
# [1, 2, 3, 4, 5, 7, 9]
```

**Note**: _We can sort the list using `list.sort()` method which is more efficient than `sorted()` method, but remember, `list.sort()` method modifies the list in place so we cannot recover the original list._

## Sorting the list in a descending order
Sorting in a descending order is as easy as sorting in an ascending order; we just pass the second argument `reverse=True`.

```py
print(sorted([1, 4, 7, 2, 9, 5, 3], reverse=True))
# [9, 7, 5, 4, 3, 2, 1]
```


## Complex Sorting with the `sorted()` function
Unlike `list.sort()` which is available in the list only, we can sort any iterable with the sorted() method. For example we can sort the dictionary, a multidimensional iterable, etc.

The following is an example of sorting the dictionary

```py
person = {
    'name': 'John Doe',
    'age': 20,
    'occupation': 'student'
}
print(sorted(person))

# ['age', 'name', 'occupation']
```
**Note**: _When we sort the dictionary, it returns the list of keys of the dictionary._

If we want to sort the dictionary and get the final result as the dictionary, then we need to sort using `dict.items()` and then regenerate the dictionary again.

```py
person = {
    'name': 'John Doe',
    'age': 20,
    'occupation': 'student'
}

print(sorted(person.items()))
# output (dict_items)
# [('age', 20), ('name', 'John Doe'), ('occupation', 'student')]


print({k:v for k,v in sorted(person.items())})
# output (dict)
# {'age': 20, 'name': 'John Doe', 'occupation': 'student'}
```

### a `key` parameter in `sorted()` function

Additionally, we can pass the `key` parameter to the `sorted()` function to do advanced sorting. for example:

```py
students = [
    ('John', 2),
    ('Eve', 4),
    ('Jennifer', 3),
    ('Adam', 1)
]
print(sorted(students, key=lambda x: x[1]))

# Output
# [('Adam', 1), ('John', 2), ('Jennifer', 3), ('Eve', 4)]
```
