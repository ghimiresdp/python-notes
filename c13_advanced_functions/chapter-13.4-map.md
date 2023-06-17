> - **created by**: Sudip Ghimire
> - **URL**: https://www.sudipghimire.com.np
> - **GitHub**: https://github.com/ghimiresdp
>
> [go to course contents](https://github.com/ghimiresdp/python-notes/)

# Chapter 13.4: The `map()` Function

**Table of Contents**

- [Chapter 13.4: The `map()` Function](#chapter-134-the-map-function)
  - [Introduction to `map()` function](#introduction-to-map-function)
  - [Using `map()` function with other functions to transform data](#using-map-function-with-other-functions-to-transform-data)
  - [Using `map()` function with lambda to transform data](#using-map-function-with-lambda-to-transform-data)
  - [Using `map()` function to manipulate 2 lists](#using-map-function-to-manipulate-2-lists)

## Introduction to `map()` function

Map function is a generator function that applies another function to elements
of the iterable that is passed as an argument. The basic structure of a `map()`
function is as follows:

```python
map(function, iterable)
map(function, iterable, *iterables)
```

The first parameter `function` is function itself that transforms the element to
the iterable. The `function` can either be a regular function or a lambda.

Reference: <https://docs.python.org/3/library/functions.html#map>

## Using `map()` function with other functions to transform data

```python
def capitalize_and_ascii_sum(word: str):
    """
    This method capitalizes the word and finds out the sum of ASCII value of
    all characters of a word
    """
    return sum(ord(x) for x in word.capitalize())


animals = ['cat', 'dog', 'cow']

transformed_data = map(capitalize_and_ascii_sum, animals)
print(list(transformed_data))  # [280, 282, 297]

```

Here the first parameter `capitalize_and_ascii_sum` is a callable that is mapped
to each data of the list `animals`.

## Using `map()` function with lambda to transform data

We can also use `lambda` instead of a function for transforming the data.

```python
numbers = [1, 2, 3, 4, 5]

squares = map(lambda x: x ** 2, numbers)
print(list(squares))  # [1, 4, 9, 16, 25]
```

Here, the `lambda` squares the number that is passed and maps the square values
of all the elements of the list `numbers`.


## Using `map()` function to manipulate 2 lists

We can also map 2 or more iterables to find out the resulting iterable. This
method is useful when we have to perform operations between different data such
as sum of each element of list.

If we pass 2 iterables of different length, it will map the value until the
shortest iterable gets exhausted.

```python
food = ['apple', 'potato', 'chicken', 'banana']
product = ['juice', 'chips', 'chilly', 'shake']

dishes = map(lambda a, b: f'{a} {b}', food, product)
print(list(dishes))  # ['apple juice', 'potato chips', 'chicken chilly', 'banana shake']
```
