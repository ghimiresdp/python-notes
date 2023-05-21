"""
JSON

- JavaScript Object Notation
- Used for data exchange throughout machines and platforms.
- It is used as data interchange format for REST APIs

- JSON contains Key Value Pairs.

- Data Types in json
    - number (9, 9.9)
    - string ("str1")
    - boolean (true, false)
    - null (Python Equivalent is None)

    - Array [1,2] (Python Equivalents are List, tuple, set)
    - Object (Python Equivalent is Dictionary)
    {"key": "value"}

    {
        "key": {
            "key": {
                "key1": value1
                "key2": value2
                "key3": [1,2]
                "key3": [
                    {"key": "Value"},
                    {"key": "Value"},
                    {"key": "Value"}
                ]
            }
        }
    }

"""


# JSON Methods in python

"""
dump    - it converts python dictionary to json file
load    - it retrieves all values from a json file and loads into a dictionary

dumps   - it is similar to dump() method, but, it just returns string instead of storing in a file
loads   - it is similar to load() method but, it converts json formatted string into a dictionary
"""


# To use json we have to import the json module
import json
from json.decoder import JSONDecodeError

# Dumping a dictionary to a file
person = {
    "name": "John Doe",
    "age": 20,
    "married": False,
    "occupation": None,
    "father":{
        "name": "John Doe Sr.",
        "age": 50,
        "childrens":("Jon", "Jane",),
    },
    5: 10.5,
}

with open('person.json', 'w') as f:
    json.dump(person, f)



# loading a json object from a file

with open('response.json', 'r') as f:
    try:
        response = json.load(f)

        print(type(response))
    except JSONDecodeError as e:
        print("The JSON file you provided is not in a correct format")


# dumping a dictionary into json string


value = json.dumps(person)

print(value)


json_string = '{"name": "Jon Doe"}'


dict2 = json.loads(json_string)

print(dict2["name"])


# dumping a file with indented key value pairs

with open('person.json', 'w') as f:
    json.dump(person, f, indent=4)
