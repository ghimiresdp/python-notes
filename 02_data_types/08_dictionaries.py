# https://sudipghimire.com.np
# %% [markdown]
"""
## Dictionary

- Dictionaries are similar to lists or sets
- They are represented by key-value pairs
- dictionaries are ordered (since python 3.7)
- they are written inside curley brackets or braces {}
- keys must be unique otherwise the later one replaces the previous key-value pair
- dictionaries are mutable.
- dictionaries can have multiple data types in their key-value pair

"""


# %% Example of dictionary
person = {
    'name': 'Spock',
    'age': 20,
    'married': False,
    'positions': ['Lieutenant', 'Captain', 'Commander']
}


# %% the duplicate key replaces the previous one

person = {
    'name': 'Spock',
    'age': 20,
    'married': False,
    'age': 21
}


# %% accessing an element of the dictionary
# it is similar to accessing an item of the list
# instead of the index, we provide the key to access the value of that key

print(person['name'])
print(person['married'])
print(person['age'])


# %% if the key doesnot exist, it gives exception

# print(person['father'])   # gives an error

# we can avoid exceptions by using `get()` method
# using the get() method, if it doesn't find any key, it returns None by default

print(person.get('name'))           # Spock
print(person.get('middle_name'))    # None

# if we want some default value to be passed, we can pass it as a second argument
print(person.get('father', False))

# occupation the default must be `student`
print(person.get('occupation', 'student'))

# if the value exists, then it is going to ignore the default value (or the second argument)

print(person.get('name', 'John Doe'))

# %% finding out the length of the dictionary

print(person.__len__())  # or
print(len(person))


# %% adding new item to the dictionary

person['gender'] = 'male'
person['occupation'] = 'Science Officer'
person['middle_name'] = 'shiva'

print(person)

# %% updating items
person['age'] = 50
person['gender'] = 'female'

# %% updating/adding multiple items

other_fields = {
    'age': 60,
    'origin': 'Vulcan',
    'species': 'Half-vulcan, half-human',
    'affiliation': 'starfleet'
}

person.update(other_fields)

person.update({
    'age': 60,
    'origin': 'Vulcan',
    'species': 'Half-vulcan, half-human',
    'affiliation': 'starfleet'
})



### 2 more fields father, mother

person.update({
    'father':'Father',
     'mother':'Mother'
})





# %% Removing an item from the dictionary

person.pop('occupation')

#popping the element again from the dictionary gives key error.

# if we want to use the popped item in the future, then we have to assign it a
# variable.
popped_item = person.pop('father')

# %% removing the last item using popitem()
# popitem method follows LIFO process (remember: push and pop)
person.popitem()

# popitem() returns keys and values as  a tuple so we can catch them if we want to use it later.
(k, v) = person.popitem() # or  # this is more preferred

# we can ignore any one of them using single underscore `_`
(_, v) = person.popitem() # we do not want key
(k, _) = person.popitem() # we do not want value


tuple_1 = person.popitem()  # store every values as a tuple

# %% looping through a dictionary

# getting only keys

for key in person:
    print(f"The key is {key}")

# %% looping through a dict to get values

for key in person:  # or person.keys()
    print(f"The {key} is {person[key]}")


# %% getting only values

for value in person.values():
    print(f'the value is {value}')


# %% Getting both keys and values of the dict

for (key, value) in person.items():
    print(f'the {key} is {value}')


# %% copy() method

spock = person.copy()
print(spock)


# %% Nested dictionaries

yoda = {
    'name': 'Yoda',
    'age': 900,
    'species': "Yoda's",
    'language': 'Galactic Basic',
    'affiliation': {
        'organization': 'Jedi',
        'member_size': 12,
        'weapons': ['Force', 'Lightsaber', 'swords', 'batons']
    },
    'weapon': 'lightsaber',
}

print(yoda['affiliation']['organization'])
print(yoda['affiliation']['weapons'][1])

# %% [markdown] other dictionary methods
"""
- `fromkeys()` method
- `setdefault()` method
- `clear()` method
"""

yoda1 = yoda.fromkeys(['name', 'age', 'language', 'father'])

# %%

yoda.setdefault('age', 910)
