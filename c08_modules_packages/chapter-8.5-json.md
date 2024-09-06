# Chapter 8.5 The `json` module

**Table of Contents**:

- [Chapter 8.5 The `json` module](#chapter-85-the-json-module)
  - [introduction to JSON](#introduction-to-json)
  - [JSON Data Types and its python equivalent](#json-data-types-and-its-python-equivalent)
  - [JSON basic Example](#json-basic-example)
  - [JSON example with nested objects](#json-example-with-nested-objects)
  - [Dumping Python dictionary into a json string or a file](#dumping-python-dictionary-into-a-json-string-or-a-file)
    - [Dumping the dictionary into JSON string](#dumping-the-dictionary-into-json-string)
    - [Dumping the dictionary into JSON file](#dumping-the-dictionary-into-json-file)
  - [Loading the JSON file or a JSON string](#loading-the-json-file-or-a-json-string)
    - [Loading the JSON string](#loading-the-json-string)
    - [Loading the JSON file](#loading-the-json-file)

## introduction to JSON

- JSON (JavaScript Object Notation) is a light weight data interchange format inspired by `Javascript` object literal
  syntax.
- A JSON file contains an object or an array that can contain different levels of nesting.
- Keys are `string` and are surrounded with double quotes `"`.

## JSON Data Types and its python equivalent

| SN | JSON Data Type | JSON Example       | Python Equivalent | Python Example     |
|----|----------------|--------------------|-------------------|--------------------|
| 1  | number         | `1`, `2.5`         | `int` or `float`  | `1`, `2.5`         |
| 2  | string         | `"John"`           | `str`             | `'john'`           |
| 3  | boolean        | `true` or `false`  | `bool`            | `True` or `False`  |
| 4  | object         | `{"key": "value"}` | `dict`            | `{'key': 'value'}` |
| 5  | arrray         | `[1,2,3]`          | `list`, `tuple`   | `[1,2,3]`          |
| 6  | null           | `null`             | `None`            | `None`             |

## JSON basic Example

```json
{
    "name": "John Doe",
    "age": 20,
    "married": true,
    "children": null
}
```

## JSON example with nested objects

```json
{
    "name": "Grade 1",
    "session": 2022,
    "class_teacher": "John Lennon",
    "students": [
        {
            "id": 1,
            "name": "John Doe",
            "subjects": [
                "Physics",
                "Mathematics"
            ]
        },
        {
            "id": 2,
            "name": "Jane Doe",
            "subjects": [
                "Chemistry",
                "Biology"
            ]
        }
    ]
}
```

## Dumping Python dictionary into a json string or a file

```python
person = {
    "name": "John Doe",
    'age': 20,
    'married': False,
    'occupation': 'programmer',
    'programming_languages': [
        {
            "name": "Python",
            "version": 3.9,
            'level': "Beginner",
        },
        {
            "name": "Java",
            "version": 17,
            'level': "Expert",
        },
        {
            "name": "C++",
            "version": 2019,
            'level': "Mid",
        },
    ]
}

```

### Dumping the dictionary into JSON string

We can dump the python dictionary or a list into JSON string using `json.dumps()` method.

```python
import json

json_str = json.dumps(person)
```

### Dumping the dictionary into JSON file

We can dump the python dictionary or a list into JSON file using `json.dump()` method.

To dump the dictionary into the json file, we need to open file in a `write mode`.

```python
import json

with open("filename.json", 'w') as file:
    json.dump(person, file)
```

The above command saves the output in the file `filename.json` inside the current working directory.

## Loading the JSON file or a JSON string

### Loading the JSON string

we can load the JSON string into python equivalent data using `json.loads()` method.

```python
import json

json_string = '{"name": "John", "age": 20}'
dict_1 = json.loads(json_string)
```

### Loading the JSON file

we can load the JSON file into python equivalent data using `json.load()` method.

To load the dictionary from the json file, we need to open file in a `read mode`.

```python
import json

with open("filename.json", 'r') as file:
    dict_1 = json.load(file)
```
