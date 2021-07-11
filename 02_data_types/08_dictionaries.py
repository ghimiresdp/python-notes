# https://sudipghimire.com.np
"""
Dictionary

- Dictionaries are similar to lists or sets
- They are represented by key-value pairs
- dictionaries are ordered (since python 3.7)
- they are written in curley brackets or braces {}
- keys must be unique otherwise the later one replaces the previous key-value pair
- dictionaries are mutable.
- dictionaries can have multiple data types in their key-value pair

"""


# %% Example of dictionary
person = {
    'name': 'Spock',
    'age': 20,
    'married': False,
    'positions':['Lieutenant', 'Captain', 'Commander']
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

# %% if the key doesnot exist, it gives exception
# we can avoid exceptions by using `get()` method
# using the get() method, if it doesn't find any key, it returns None by default
print(person.get('name'))
print(person.get('father'))

# if we want some default value to be passed, we can pass it as a second argument
print(person.get('father', 'not specified in the dictionary'))

# %% finding out the length of the dictionary

print(person.__len__())  # or
print(len(person))


# %% adding new item to the dictionary

person['gender'] = 'male'
person['occupation'] = 'Science Officer'
print(person)

# %% updating items
person['age'] = 50

# %% updating/adding multiple items

person.update({
    'age': 60,
    'origin': 'Vulcan',
    'species': 'Half-vulcan, half-human',
    'affiliation': 'starfleet'
})


# %% Removing an item from the dictionary

person.pop('occupation')

# %% removing the last item using popitem()
# popitem method follows LIFO process
person.popitem()

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

for (k, v) in person.items():
    print(f'the {k} is {v}')


# %% copy() method

spock = person.copy()
print(spock)


# %% Nested dictionaries

yoda = {
    'name': 'Yoda',
    'age': 900,
    'species': 'Yoda\'s',
    'language': 'Galactic Basic',
    'affiliation': {
        'organization': 'Jedi',
        'member_size': 12,
        'weapons': ['Force', 'Lightsaber', 'swords', 'batons']
    },
    'weapon': 'lightsaber',
}

print(yoda['affiliation']['organization'])


# %% other dictionary methods
"""
- copy()
- fromkeys()
- setdefault()
- clear()
"""
